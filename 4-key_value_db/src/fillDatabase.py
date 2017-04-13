import re as regex

import redis

# REDIS
REDIS = redis.StrictRedis(host='localhost', port=6379, db=0)
REDIS_PIPE = REDIS.pipeline()

# FILE
FILE_PATH = 'resources/plz_mini.data'

# PATTERN
KEY_PATTERN = '"([_a-zA-Z]+)"'
NUM_PATTERN = '.\-0-9'


def get_dictionary_from_string(string):
    """Returns a Map/Dictionary from a String with KEY VALUE pairs"""
    result = {}
    # Look for "<KEY>" : "<VALUE>"
    for match in regex.findall(KEY_PATTERN + ' : "([ 0-9a-zA-Z]+)"', string):
        result[match[0]] = match[1]
    # Look for "<KEY>" : <NUM_VALUE>
    for match in regex.findall(KEY_PATTERN + ' : ([.\-0-9]+)', string):
        result[match[0]] = float(match[1])
    # Look for "<KEY>" : [<NUM_VALUES, ... >]
    for match in regex.findall(KEY_PATTERN + ' : \[([.,\- 0-9]+)\]', string):
        result[match[0]] = [float(i) for i in (match[1].split(','))]

        print(result)
    return result


def save_file(file_path):
    dict_from_line = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Convert line to Map/Dictionary
            dict_from_line = get_dictionary_from_string(line)

            # SAVE IN REDIS
            identifier = dict_from_line.pop('_id')
            state = dict_from_line.pop('state')
            city = dict_from_line.pop('city')
            key = identifier + ':' + state + ':' + city
            REDIS.set(key + '#pop', dict_from_line['pop'])
            REDIS.set(key + '#loc', dict_from_line['loc'])


# GET FROM FILE
save_file(FILE_PATH)
