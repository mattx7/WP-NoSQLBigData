import happybase


class Constants:
    """Holds constants"""

    def __init__(self):
        pass

    # HBASE
    CONNECTION = happybase.Connection('localhost', autoconnect=False)
    TABLE_NAME = 'plz'
    TABLE = CONNECTION.table(TABLE_NAME)
    # FILE
    FILE_PATH = '../../resources/plz.data'
    RESOURCE_PATH = '../../resources/'

    # DEBUG
    VERBOSE = False
