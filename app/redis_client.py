import os
import redis

REDIS_URL = os.getenv("REDIS_URL")

if not REDIS_URL:
    raise RuntimeError("REDIS_URL not set")

rdb = redis.Redis.from_url(
    REDIS_URL,
    decode_responses=True,
)

def redis_ok():
    try:
        rdb.ping()
        return True
    except Exception as e:
        print("Redis error:", e)
        return False
