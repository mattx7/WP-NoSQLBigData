import re as regex

from _7_mongo_db.src.data_access.Constants import Constants


class Saver:
    """Saves into redis-database"""

    def __init__(self):
        self.keyPattern = '"([_a-zA-Z]+)"'

    def save_file_from_resource(self, file_name):
        """Save all from existing file in resource"""
        return self.save_file(Constants.RESOURCE_PATH + file_name)

    def save_file(self, file_path):
        """Save all from file in mongo-db"""
        count = 0
        with open(file_path, 'r') as file:
            for line in file:
                # Convert line to Map/Dictionary
                dict_from_line = self.__get_dictionary_from_string(line)
                # SAVE IN MONGO
                self.__save(dict_from_line)
                count = count + 1
        return count

    def __save(self, dict):
        """Saves a dictionary into the database"""
        Constants.COLLECTION.insert_one(dict)
        if Constants.VERBOSE:
            print(str(dict))

    def __get_dictionary_from_string(self, string):
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
        return result

    def delete_all(self):
        """Clears the database"""
        Constants.MONGO_CLIENT.drop_database(Constants.MONGO_DB_NAME)
