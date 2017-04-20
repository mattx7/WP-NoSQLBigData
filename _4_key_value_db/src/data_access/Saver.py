import re as regex

from _4_key_value_db.src.data_access.Constants import Constants


class Saver:
    """Saves into redis-database"""

    def __init__(self):
        self.keyPattern = '"([_a-zA-Z]+)"'

    def save_file(self, file_path):
        """Save all from file in redis database"""
        with open(file_path, 'r') as file:
            for line in file:
                # Convert line to Map/Dictionary
                dict_from_line = self.get_dictionary_from_string(line)
                # SAVE IN REDIS
                self.save(dict_from_line)

    def save(self, dict):
        # get key-values
        identifier = dict.pop('_id')
        state = dict.pop('state')
        city = dict.pop('city')
        # create key
        key = identifier + ':' + state + ':' + city

        # Add Values
        Constants.CONNECTION.set(key + '#pop', dict['pop'])
        Constants.CONNECTION.set(key + '#loc', dict['loc'])

    def get_dictionary_from_string(self, string):
        """Returns a Map/Dictionary from a String with KEY VALUE pairs"""
        result = {}
        # Look for "<KEY>" : "<VALUE>"
        for match in regex.findall(self.keyPattern + ' : "([\- 0-9a-zA-Z]+)"', string):
            result[match[0]] = match[1]
        # Look for "<KEY>" : <NUM_VALUE>
        for match in regex.findall(self.keyPattern + ' : ([.\-0-9]+)', string):
            result[match[0]] = float(match[1])
        # Look for "<KEY>" : [<NUM_VALUES, ... >]
        for match in regex.findall(self.keyPattern + ' : \[([.,\- 0-9]+)\]', string):
            result[match[0]] = [float(i) for i in (match[1].split(','))]

            print(result)
        return result

        # save_file(FILE_PATH)