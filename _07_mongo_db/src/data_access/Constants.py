from pymongo import MongoClient


class Constants:
    """Holds constants"""

    def __init__(self):
        pass

    # MONGO-DB
    MONGO_DB_NAME = 'database'
    MONGO_COLLECTION_NAME = 'collection'
    MONGO_CLIENT = MongoClient(port=26016)
    DB = MONGO_CLIENT[MONGO_DB_NAME]
    COLLECTION = DB[MONGO_COLLECTION_NAME]

    # FILE
    FILE_PATH = '../../resources/plz.data'
    RESOURCE_PATH = '../../resources/'

    # DEBUG
    VERBOSE = False
