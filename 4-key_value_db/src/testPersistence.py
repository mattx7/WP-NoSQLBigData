import re as regex

import redis

# https://pypi.python.org/pypi/redis

db = redis.StrictRedis(host='localhost', port=6379, db=0)
pipe = db.pipeline()


def dict_from_string(str):
    result = {}
    for match in regex.findall('"([_0-9a-zA-Z]*)" : "([0-9a-zA-Z]*)"', str):
        result[match[0]] = match[1]
    return result


# GET FROM FILE
dict_from_line = {}
with open('resources/plz_mini.data', 'r') as inf:
    for line in inf:
        dict_from_line = dict_from_string(line)
        # SAVE IN REDIS
        id = dict_from_line.pop("_id")
        db.hmset(id, dict_from_line)

result = db.hgetall("01001")
print(result)
