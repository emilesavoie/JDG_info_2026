import express, { Request, Response } from 'express';
import { createClient, RedisClientType } from 'redis';
import { checkRedisHealth, getValue, listKeys, setValue } from './redis-client';
import * as fs from 'fs';

type Config = {
  network: string;
};

// Read configuration file 
// -- Not used currently, left here if needed by student
const data = fs.readFileSync('./my-deployment-configs.json', 'utf-8');
const config: Config = JSON.parse(data);
const ownNetworkName = config.network;

const app = express();
const port = process.env.PORT || 3000;

let redisClient: RedisClientType | undefined;

app.use(express.json());

app.get('/', (req: Request, res: Response) => {
  res.send('Hello, TypeScript Express!');
});

app.get('/health', async (req: Request, res: Response) => {
  const isHealthy = await checkRedisHealth(redisClient);
  if (isHealthy) {
    res.status(200).send('OK');
  } else {
    res.status(500).send('Redis is down');
  }
});

app.post('/elect-new', async (req: Request, res: Response) => {
  let { domain, port } : { domain: string | undefined, port: number | undefined } = req.body;

  if (!domain) {
    return res.status(400).send('Domain is required');
  }

  if (!port) {
    return res.status(400).send('Port is required');
  } 

  try {
    const url = `redis://${domain}:${port}`;
    console.log(`Electing new leader at "${url}"`);
    if(redisClient && redisClient.isOpen) {
      await redisClient.quit();
    }
    redisClient = createClient({ url });
    await redisClient.connect();
  } catch (error) {
    console.error('Error electing new leader:', error);
    redisClient?.destroy();
    redisClient = undefined;
    return res.status(500).send('Failed to elect new leader');
  }

  // Logic to elect a new leader using the provided address
  res.status(201).send('New leader elected');
});

app.post('/set-value', async (req: Request, res: Response) => {
  const { key, value } = req.body;
  if (!key || !value) {
    return res.status(400).send('Key and value are required');
  }
  if(!redisClient) {
    return res.status(500).send('Redis client is not initialized');
  }
  
  if(!checkRedisHealth(redisClient)) {
    return res.status(500).send('Redis client is not healthy');
  }

  try {
    await setValue(redisClient, key, value);
  } catch (error) {
    console.error('Error setting value in Redis:', error);
    return res.status(500).send('Failed to set value');
  }
  res.status(201).send('Value set');
});

app.get('/get-value/:key', async (req: Request, res: Response) => {
  if(!redisClient) {
    return res.status(500).send('Redis client is not initialized');
  }
  const { key } = req.params;

  try {
    const value = await getValue(redisClient, key);
    if (value) {
      res.status(200).send(value);
    } else {
      res.status(404).send('Value not found');
    }
    return;
  } catch (error) {
    console.error('Error getting value from Redis:', error);
    return res.status(500).send('Failed to get value');
  }
});

app.get('/keys', async (req: Request, res: Response) => {
  if(!redisClient) {
    return res.status(500).send('Redis client is not initialized');
  }

  try {
    const keys = await listKeys(redisClient);
    res.status(200).send(keys);
  } catch (error) {
    console.error('Error listing keys from Redis:', error);
    return res.status(500).send('Failed to list keys');
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
