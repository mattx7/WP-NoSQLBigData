import redis

# https://pypi.python.org/pypi/redis

db = redis.StrictRedis(host='localhost', port=6379, db=0)
pipe = db.pipeline()

d = {}
# with open('resources/plz_mini.data', 'r') as f:
#     for line in f:
#        db.hmset("pythonDict", line)

# with open('resources/plz_mini.data') as data_file:
#     test_data = json.load(data_file)
# db.set('test_json', test_data)

# GET FROM FILE
dicts_from_file = []
with open('resources/plz_mini.data', 'r') as inf:
    for line in inf:
        dicts_from_file.append(eval(line))

# SAVE IN REDIS
# with dicts_from_file as line:
#     db.hmset('key',line)
