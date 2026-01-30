import os
import redis

REDIS_URL = os.getenv("REDIS_URL")

rdb = redis.Redis.from_url(
    REDIS_URL,
    decode_responses=True,
)

def redis_ok():
    try:
        return rdb.ping()
    except Exception as e:
        print("Redis error:", e)
        return False
