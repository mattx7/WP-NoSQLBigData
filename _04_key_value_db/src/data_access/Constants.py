import redis


class Constants:
    """Holds constants"""

    def __init__(self):
        pass

    # REDIS
    CONNECTION = redis.StrictRedis(host='localhost', port=6379, db=0)
    PIPE = CONNECTION.pipeline()

    # FILE
    FILE_PATH = '../../resources/plz.data'
    RESOURCE_PATH = '../../resources/'

    # DEBUG
    VERBOSE = False
