from os import environ
import redis

REDIS_HOST = environ.get("REDIS_HOST") if environ.get("REDIS_HOST") else "localhost"
REDIS_PORT = int(environ.get("REDIS_PORT") if environ.get("REDIS_PORT") else 6379)

redis_conn = redis.StrictRedis(host = REDIS_HOST, port = REDIS_PORT)
