from pymongo import MongoClient

# DEF
HOST = '172.17.0.2'
PORT = 27017
MONGO_DB_NAME = 'database'
MONGO_COLLECTION_NAME = 'collection'

# MONGO-DB
MONGO_CLIENT = MongoClient(host=HOST, port=PORT)
DB = MONGO_CLIENT[MONGO_DB_NAME]
COLLECTION = DB[MONGO_COLLECTION_NAME]

# FILE
FILE_NAME = 'plz.data'

# DEBUG
VERBOSE = False
