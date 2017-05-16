import re as regex

import RedisConstants as Constants

keyPattern = '"([_a-zA-Z]+)"'


def save_file(file_path):
    """Save all from a file in redis database"""
    count = 0
    with open(file_path, 'r') as a_file:
        for line in a_file:
            # Convert line to Map/Dictionary
            dict_from_line = get_dictionary_from_string(line)
            # SAVE IN REDIS
            save(dict_from_line)
            count += 1
    return count


def save(key_value):
    """Saves a dictionary into the database"""

    # get key-values
    identifier = key_value['_id']
    state = key_value['state']
    city = key_value['city']

    # create key
    key = identifier + ':' + state + ':' + city

    # Add Values
    Constants.CONNECTION.set(key + '#pop', key_value['pop'])
    Constants.CONNECTION.set(key + '#loc', key_value['loc'])

    if Constants.VERBOSE:
        print(str(key_value))


def get_dictionary_from_string(string):
    """Returns a Map/Dictionary from a String with KEY VALUE pairs"""
    result = {}
    # Look for "<KEY>" : "<VALUE>"
    for match in regex.findall(keyPattern + ' : "([\- 0-9a-zA-Z]+)"', string):
        result[match[0]] = match[1]
    # Look for "<KEY>" : <NUM_VALUE>
    for match in regex.findall(keyPattern + ' : ([.\-0-9]+)', string):
        result[match[0]] = float(match[1])
    # Look for "<KEY>" : [<NUM_VALUES, ... >]
    for match in regex.findall(keyPattern + ' : \[([.,\- 0-9]+)\]', string):
        result[match[0]] = [float(i) for i in (match[1].split(','))]
    return result


def delete_all():
    """Clears the database"""
    Constants.CONNECTION.flushall()
    print('Database cleared!')
