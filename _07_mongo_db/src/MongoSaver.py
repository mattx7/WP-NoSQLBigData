import re as regex

import MongoConstants as Constants

keyPattern = '"([_a-zA-Z]+)"'


def save_file(file_path):
    """Save all from file in mongo-db"""
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            # Convert line to Map/Dictionary
            dict_from_line = __get_dictionary_from_string(line)
            # SAVE IN MONGO
            __save(dict_from_line)
            count += 1
    return count


def __save(key_value):
    """Saves a dictionary into the database"""
    Constants.COLLECTION.insert_one(key_value)
    if Constants.VERBOSE:
        print(str(key_value))


def __get_dictionary_from_string(string):
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
    Constants.MONGO_CLIENT.drop_database(Constants.MONGO_DB_NAME)
    print('Database cleared!')
