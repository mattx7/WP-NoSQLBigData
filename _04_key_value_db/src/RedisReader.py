import re as regEx

import RedisConstants as Constants


def filter_and_return(id, state, city, return_value):
    """Filter by id, state and city. '' is possible. return_values could be id, state or city"""

    keys = Constants.CONNECTION.keys(id + '*:' + state + '*:*' + city + '*#*')
    result = set()

    for key in keys:
        tmp = regEx.search('(.*):(.*):(.*)#', str(key))

        if return_value == 'zip':
            result.add(tmp.group(1))
        elif return_value == 'state':
            result.add(tmp.group(2))
        elif return_value == 'city':
            result.add(tmp.group(3))

    return result
