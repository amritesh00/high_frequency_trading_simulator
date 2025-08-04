# app/redis_client.py

import redis
import os

# Get Redis URL from environment variable (Render → Environment tab)
redis_url = os.getenv("REDIS_URL")

# Create Redis client from the URL with decode_responses enabled
rdb = redis.Redis.from_url(
    redis_url,
    decode_responses=True
)

# Optional: Health check on startup
try:
    rdb.ping()
    print("✅ Successfully connected to Redis")
except Exception as e:
    print("❌ Redis connection failed:", e)
