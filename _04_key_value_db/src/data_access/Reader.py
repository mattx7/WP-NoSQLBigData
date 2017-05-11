import re as regEx

from _04_key_value_db.src.data_access.Constants import Constants


class Reader:
    """Reads from Database"""

    def __init__(self):
        pass

    @staticmethod
    def filter_and_return(id, state, city, return_value):
        """Filter by id, state and city. '' is possible. return_values could be id, state or city"""

        keys = Constants.CONNECTION.keys(id + '*:' + state + '*:*' + city + '*#*')
        result = set()

        for key in keys:
            tmp = regEx.search('(.*):(.*):(.*)#', str(key, 'utf-8'))

            if return_value == 'id':
                result.add(tmp.group(1))
            elif return_value == 'state':
                result.add(tmp.group(2))
            elif return_value == 'city':
                result.add(tmp.group(3))

        return result
