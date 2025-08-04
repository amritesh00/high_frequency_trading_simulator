import redis
import os
from urllib.parse import urlparse

redis_url = urlparse(os.getenv("REDIS_URL", "redis://localhost:6379"))

rdb = redis.Redis(
    host=redis_url.hostname,
    port=redis_url.port,
    password=redis_url.password,
    decode_responses=True
)

