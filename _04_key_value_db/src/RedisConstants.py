import redis

# REDIS
HOST = '172.17.0.2'
PORT = 6379
CONNECTION = redis.StrictRedis(host=HOST, port=PORT, db=0)
PIPE = CONNECTION.pipeline()

# FILE
FILE_NAME = 'plz.data'

# DEBUG
VERBOSE = False
