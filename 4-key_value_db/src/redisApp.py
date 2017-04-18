import getopt as getOpt
import re as regEx
import sys

import redis

# https://pypi.python.org/pypi/redis

# REDIS
REDIS = redis.StrictRedis(host='localhost', port=6379, db=0)
REDIS_PIPE = REDIS.pipeline()

VERBOSE = False


# result = REDIS.get('01001:MA:AGAWAM#loc')
# print(result)
#
# # print all keys
# for res in REDIS.keys('01001*'):
#     print(res)


def filterAndReturn(id, state, city, return_value):
    """Filter by id, state and city. '' is possible. return_values could be id, state or city"""
    keys = REDIS.keys(id + '*:' + state + '*:*' + city + '*#*')
    result = set()
    for key in keys:
        tmp = regEx.search('(.*):(.*):(.*)#', str(key, 'utf-8'))
        if return_value == 'id':
            result.add(tmp.group(1))
        elif return_value == 'state':
            result.add(tmp.group(2))
        elif return_value == 'city':
            result.add(tmp.group(3))
    return result


# print('Result:')
# for result in filterAndReturn('', '', 'HAMBURG', 'id'):
#     print(result)


def usage():
    print("Usage: Filter with [-i,--id] [-s,--state] [-c,--city] and [-r,--return] could be 'id', 'state' or 'city' ")


def main():
    id = ''
    state = ''
    city = ''
    return_value = 'id'
    # parse command line options
    try:
        opts, args = getOpt.getopt(sys.argv[1:], "hi:s:c:r:", ["help", "id=", "state=", "city=", "return="])
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
        elif o in ("-r", "--return"):
            return_value = a
        else:
            assert False, "unhandled option"
    for result in filterAndReturn(id, state, city, return_value):
        print(result)


if __name__ == "__main__":
    main()
