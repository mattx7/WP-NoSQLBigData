import getopt as getOpt
import re as regEx
import sys

import redis

# https://pypi.python.org/pypi/redis

# REDIS
REDIS = redis.StrictRedis(host='localhost', port=6379, db=0)
REDIS_PIPE = REDIS.pipeline()

VERBOSE = False

result = REDIS.get('01001:MA:AGAWAM#loc')
print(result)

# print all keys
for res in REDIS.keys('01001*'):
    print(res)


def filterAndReturn(id, state, city, return_value):
    """Filter by id, state and city. '' is possible. return_values could be all, id, state or city"""
    keys = REDIS.keys(id + '*:' + state + '*:*' + city + '*#*')
    result = set()
    for key in keys:
        tmp = regEx.search('(.*):(.*):(.*)#', str(key, 'utf-8'))
        for return_value in return_values:
            dict = {}
            if return_value == 'all':
                result.append({'id': tmp.group(1), 'state': tmp.group(2), 'city': tmp.group(3)})
                break
            elif return_value == 'id':
                dict.update({'id': tmp.group(1)})
            elif return_value == 'state':
                dict.update({'state': tmp.group(2)})
            elif return_value == 'city':
                dict.update({'city': tmp.group(3)})
            result.append(dict)
    return result


print('Result:')
for result in filterAndReturn('', '', 'HAMBURG', 'id'):
    print(result)


def usage():
    print("Usage:")


def main():
    id = ''
    state = ''
    city = ''
    return_values = set()
    # parse command line options
    try:
        opts, args = getOpt.getopt(sys.argv[1:], "h", ["help"])
    except getOpt.GetoptError as err:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif o in ("-i", "--id"):
            id = a
        elif o in ("-s", "--state"):
            state = a
        elif o in ("-c", "--city"):
            city = a
        else:
            assert False, "unhandled option"
    if len(args) <= 1:
        usage()
        sys.exit(2)
    else:
        filterAndReturn(id, state, city, args)


if __name__ == "__main__":
    main()
