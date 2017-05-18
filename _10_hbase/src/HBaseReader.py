import HBaseConstants as Constants


def find_and_select(zipcode, state, city, selected):
    """Filter by id, state and city. '' is possible. return_values could be id, state or city"""

    found_values = []
    if zipcode != "":
        for key, data in Constants.TABLE.scan(row_prefix=bytes(zipcode, 'utf8')):
            found_values.append(data)
    else:
        col = ("state" if state != "" else "city")
        regEx = (state if state != "" else city)
        a_filter = "SingleColumnValueFilter('family', '" + col + "', =, 'regexstring:^" + regEx + "$')"
        for key, data in Constants.TABLE.scan(filter=a_filter):
            found_values.append(data)

    # get values
    result = set()
    for key_value in found_values:
        if Constants.VERBOSE:
            print("FOUND: " + str(key_value))
        # select
        if selected == 'zip':
            result.add(key_value[b'family:_id'])
        elif selected == 'state':
            result.add(key_value[b'family:state'])
        elif selected == 'city':
            result.add(key_value[b'family:city'])

    return result
