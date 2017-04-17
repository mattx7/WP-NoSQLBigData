import re as regex

import redis

# https://pypi.python.org/pypi/redis

# REDIS
REDIS = redis.StrictRedis(host='localhost', port=6379, db=0)
REDIS_PIPE = REDIS.pipeline()

result = REDIS.get('01001:MA:AGAWAM#loc')
print(result)

# print all keys
for res in REDIS.keys('01001*'):
    print(res)


def get_by(id, state, city, returnValue):
    """Filter by id, state and city, and returns id, state or city"""
    keys = REDIS.keys(id + '*:' + state + '*:*' + city + '*#*')
    cities = set()
    for key in keys:
        tmp = regex.search('(.*):(.*):(.*)#', str(key, 'utf-8'))
        if returnValue == 'id':
            cities.add(tmp.group(1))
        elif returnValue == 'state':
            cities.add(tmp.group(2))
        elif returnValue == 'city':
            cities.add(tmp.group(3))
    return cities


print('Result:')
for result in get_by('', '', 'HAMBURG', 'id'):
    print(result)
