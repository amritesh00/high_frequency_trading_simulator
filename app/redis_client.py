import os
import redis

REDIS_HOST = "redis-17677.c326.us-east-1-3.ec2.cloud.redislabs.com"
REDIS_PORT = 17677
REDIS_USERNAME = "default"
REDIS_PASSWORD = "Heatma@009"

rdb = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    username=REDIS_USERNAME,
    password=REDIS_PASSWORD,
    ssl=True,
    ssl_cert_reqs=None,
    decode_responses=True,
)

# Optional: test lazily (do NOT crash app)
def redis_ping():
    try:
        return rdb.ping()
    except Exception as e:
        print("Redis connection failed:", e)
        return False
