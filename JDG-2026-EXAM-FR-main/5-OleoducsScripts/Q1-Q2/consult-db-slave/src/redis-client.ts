import { createClient, RedisClientType } from 'redis';

// Create and configure Redis client
//const redisClient = createClient({ url: 'redis://localhost:6379' });
//redisClient.on('error', (err) => console.log('Redis Client Error', err));

// Connect to Redis
//await redisClient.connect();

// Function to set a key-value pair in Redis
export const setValue = async (client: RedisClientType,key: string, value: string): Promise<void> => {
  await client.set(key, value);
};

export const listKeys = async (client: RedisClientType): Promise<string[]> => {
  return client.keys('*');
};

// Function to retrieve a value by key from Redis
export const getValue = async (client: RedisClientType, key: string): Promise<string | null> => {
  return client.get(key);
};

export const checkRedisHealth = async (client: RedisClientType | undefined): Promise<boolean> => {
  if (!client) return false;

  try {
    await client.set('health', 'ok');
    const reply = await client.get('health');
    return reply === 'ok';
  } catch (error) {
    console.error('Redis Health Check Failed:', error);
    return false;
  }
};
