import redis
import os
from urllib.parse import urlparse

redis_url = urlparse(os.getenv("REDIS_URL"))

rdb = redis.Redis(
    host=redis_url.hostname,
    port=redis_url.port,
    password=redis_url.password,
    ssl=True,
    ssl_cert_reqs=None,
    decode_responses=True
)

# Verify connection once
rdb.ping()
