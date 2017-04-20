import redis

# https://pypi.python.org/pypi/redis

# REDIS
REDIS = redis.StrictRedis(host='localhost', port=6379, db=0)
REDIS_PIPE = REDIS.pipeline()

REDIS.set('foo', 'bar')
REDIS.get('foo')

result = REDIS.get('01001:MA:AGAWAM#loc')
print(result)

for res in REDIS.keys('01001*'):
    print(res)

# Delete all
REDIS.flushall()
