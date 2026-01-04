import { error } from 'console';
import { randomInt } from 'crypto';
import express, { Request, Response } from 'express';
import fs from 'fs';

const app = express();
const port = process.env.PORT || 3001;

app.use(express.json());

type Config = {
  servers: Array<ServerAddress>;
};
type ServerAddress = {
  domain: string;
  port: number;
  protocol: string;
  redisPort: number;
}

// Currently used, but could be replaced by another type of logic
let config: Config = JSON.parse(fs.readFileSync('./my-deployment-configs.json', 'utf-8'));
let server_addresses: ServerAddress[] = config.servers;
let currentRedisLeaderIndex = -1;


async function callElect(serverToCall: ServerAddress, redisServerDomain: string) {
  // Determine which domain the Slave will use, only used in body
  let domain = redisServerDomain;
  try {
    // Uses localhost if they match
    if (serverToCall.domain === redisServerDomain) {
      domain = "localhost";
    }
    const fetchString = `${serverToCall.protocol}://${serverToCall.domain}:${serverToCall.port}/elect-new`;
    console.log(`Calling elect on ${fetchString}`);
    console.log(`With body: { domain: ${domain}, port: 6379 }`);
    await fetch(fetchString, {
      method: "post",
      body: JSON.stringify({ domain: domain, port: 6379 }), // It uses its own domain (localhost)
      headers: {
        'Content-Type': 'application/json'
        }
      });
    } catch (error) {
      console.error(`Failed to elect new server at ${serverToCall.protocol}://${serverToCall.domain}:${serverToCall.port}/elect-new:`, error);
    }
}

// This route is for electing a new Redis leader, so there is only 1 running at a time
function electNewServerAsRedis() {
  currentRedisLeaderIndex += 1;
  if (currentRedisLeaderIndex >= server_addresses.length) {
    currentRedisLeaderIndex = 0;
  }

  console.log("electNewServerAsRedis:Current Redis Leader:", server_addresses[currentRedisLeaderIndex]);

  server_addresses.forEach(async element => {
    await callElect(element, server_addresses[currentRedisLeaderIndex].domain);
  });
}

// Random Route for tests, can be removed
app.get('/', (req: Request, res: Response) => {
  res.send('Hello, TypeScript Express!');
});


async function rerouteRequest(req: Request, res: Response, retryCount: number = 0) {
  if(retryCount > 5) {
    console.error("Max retry count reached, returning error.");
    res.status(500).send('Internal Server Error');
    return;
  }
  const whichServer = randomInt(server_addresses.length);
  try {
    const address = server_addresses[whichServer].protocol 
      + '://' + server_addresses[whichServer].domain
      + ':' + server_addresses[whichServer].port
      + '/' + req.params[0];

    console.log(`Rerouting request to server: ${address}`);
    // console.log(`Request body: ${JSON.stringify(req.body)}`);
    const rep = await fetch(
      address,
      {
        method: req.method,
        body: req.method === "POST" ? JSON.stringify(req.body) : undefined,
        headers: {
          'Content-Type': 'application/json'
        }
      }
    );

    return rep;
  } catch (error) {
    console.error(`Error fetching from the server ${whichServer} with error: `, error);
    console.log(`Retrying request on a different server...`);
    return rerouteRequest(req, res, retryCount + 1);
  }
}

app.all(new RegExp('/api/(.*)'), async (req: Request, res: Response) => {
  // Path after the /api/: req.params.path
  console.log(`Received request for path: ${req.params[0]}`);

  const response = await rerouteRequest(req, res, 0);

  if(!response) {
    res.status(500).send('Internal Server Error');
    return;
  }

  res.status(response.status).send(await response.text());
});

app.get('/leader', (req: Request, res: Response) => {
  res.send(server_addresses[currentRedisLeaderIndex]);
})

app.post('/leader', (req: Request, res: Response) => {
  // Logic to handle leader election
  electNewServerAsRedis();
  res.send('Leader election triggered');
});

app.post('/register', (req: Request, res: Response) => {
  const { domain, port, protocol, redisPort } = req.body;
  if (!domain || !port || !protocol || !redisPort) {
    res.status(400).send('Missing required fields: domain, port, protocol, redisPort');
    return;
  }
  server_addresses.push({ domain, port, protocol, redisPort });
  console.log(`Registered new server: ${domain}:${port} with protocol ${protocol} and redisPort ${redisPort}`);
  res.send('Server registered successfully');
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
  // Wait 10 seconds before electing a new Redis leader
  setTimeout(() => {
    console.log("Starting initial Redis leader election...");
    electNewServerAsRedis();
  }, 10000);
});
