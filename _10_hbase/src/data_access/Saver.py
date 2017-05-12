import re as regex

from Constants import Constants


class Saver:
    """Saves into hbase"""

    def __init__(self):
        self.keyPattern = '"([_a-zA-Z]+)"'

    def save_file_from_resource(self, file_name):
        """Save all from existing file in resource"""
        return self.save_file(Constants.RESOURCE_PATH + file_name)

    def save_file(self, file_path):
        """Save all from file in hbase"""
        count = 0
        is_table_created = False

        with open(file_path, 'r') as a_file:
            for line in a_file:

                # Convert line to Map/Dictionary
                key, dict_from_line = self.__get_key_and_dict_from_string(line)

                # Build table JUST ONCE
                if not is_table_created:
                    self.__build_table()
                    is_table_created = True

                # SAVE IN HBASE
                self.__save(key, dict_from_line)
                count += 1

        return count

    def __save(self, row, key_value):
        """Saves a dictionary into the database"""
        byte_dict = {}
        for k, v in key_value.iteritems():
            byte_dict[bytes('family' + ':' + k)] = bytes(v)
        Constants.TABLE.put(bytes(row), byte_dict)
        if Constants.VERBOSE:
            print(str(row) + " -> " + str(key_value))

    def __build_table(self):
        families = {}
        families.update({
            'family': dict()  # use defaults
        })
        try:
            Constants.CONNECTION.create_table(Constants.TABLE_NAME, families)
        except:
            pass

    def __get_key_and_dict_from_string(self, string):
        """Returns a Map/Dictionary from a String with KEY VALUE pairs"""
        key = None
        result = {}

        # Look for key
        for match in regex.findall('"(_id)" : "([0-9]+)"', string):
            key = match[1]
            break

        # Look for "<KEY>" : "<VALUE>"
        for match in regex.findall(self.keyPattern + ' : "([\- 0-9a-zA-Z]+)"', string):
            result[match[0]] = match[1]

        # Look for "<KEY>" : <NUM_VALUE>
        for match in regex.findall(self.keyPattern + ' : ([.\-0-9]+)', string):
            result[bytes(match[0])] = bytes(float(match[1]))

        # Look for "<KEY>" : [<NUM_VALUES, ... >]
        for match in regex.findall(self.keyPattern + ' : \[([.,\- 0-9]+)\]', string):
            result[bytes(match[0])] = bytes([float(i) for i in (match[1].split(','))])

        return key, result

    def delete_all(self):
        """Clears the database"""
        Constants.CONNECTION.disable_table(Constants.TABLE_NAME)
        Constants.CONNECTION.delete_table(Constants.TABLE_NAME)
        print('Database deleted!')
