import happybase

# DEF
HOST = '172.17.0.2'

# HBASE
CONNECTION = happybase.Connection(HOST, autoconnect=True)
TABLE_NAME = 'plz'
TABLE = CONNECTION.table(TABLE_NAME)

# FILE
FILE_NAME = 'plz.data'

# DEBUG
VERBOSE = False
