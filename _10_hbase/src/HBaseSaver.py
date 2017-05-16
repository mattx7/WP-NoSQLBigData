import re as regex

import HBaseConstants as Constants

keyPattern = '"([_a-zA-Z]+)"'


def save_file(file_path):
    """Save all from file in hbase"""
    count = 0
    is_table_created = False

    with open(file_path, 'r') as a_file:
        for line in a_file:

            # Convert line to Map/Dictionary
            key, dict_from_line = __get_key_and_dict_from_string(line)

            # Build table JUST ONCE
            if not is_table_created:
                __build_table()
                is_table_created = True

            # SAVE IN HBASE
            __save(key, dict_from_line)
            count += 1

    return count


def __save(row, key_value):
    """Saves a dictionary into the database"""
    byte_dict = {}
    for k, v in key_value.items():
        byte_key = bytes('family:' + str(k), 'utf8')

        if isinstance(v, str):
            byte_value = bytes(v, 'utf8')
        elif isinstance(v, float):
            byte_value = bytearray(v)
        else:
            break

        byte_dict[byte_key] = byte_value

    Constants.TABLE.put(bytes(row, 'utf8'), byte_dict)
    if Constants.VERBOSE:
        print(str(row) + " -> " + str(key_value))


def __build_table():
    families = {}
    families.update({
        'family': dict()  # use defaults
    })
    try:
        Constants.CONNECTION.create_table(Constants.TABLE_NAME, families)
    except:
        pass


def __get_key_and_dict_from_string(string):
    """Returns a Map/Dictionary from a String with KEY VALUE pairs"""
    key = None
    result = {}

    # Look for key
    for match in regex.findall('"(_id)" : "([0-9]+)"', string):
        key = match[1]
        break

    # Look for "<KEY>" : "<VALUE>"
    for match in regex.findall(keyPattern + ' : "([\- 0-9a-zA-Z]+)"', string):
        result[match[0]] = match[1]

    # Look for "<KEY>" : <NUM_VALUE>
    for match in regex.findall(keyPattern + ' : ([.\-0-9]+)', string):
        result[match[0]] = match[1]

    # Look for "<KEY>" : [<NUM_VALUES, ... >]
    for match in regex.findall(keyPattern + ' : \[([.,\- 0-9]+)\]', string):
        result[match[0]] = [float(i) for i in (match[1].split(','))]

    return key, result


def delete_all():
    """Clears the database"""
    Constants.CONNECTION.disable_table(Constants.TABLE_NAME)
    Constants.CONNECTION.delete_table(Constants.TABLE_NAME)
    print('Database deleted!')
