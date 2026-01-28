import redis
import os
from urllib.parse import urlparse

redis_url = urlparse(os.getenv("REDIS_URL"))

rdb = redis.Redis(
    host=redis_url.hostname,
    port=redis_url.port,
    username=redis_url.username,   # IMPORTANT
    password=redis_url.password,
    decode_responses=True
)
