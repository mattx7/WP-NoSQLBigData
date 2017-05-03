from _7_mongo_db.src.data_access.Constants import Constants


class Reader:
    """Reads from Database"""

    def __init__(self):
        pass

    def find_and_select(self, zipcode, state, city, selected):
        """Filter by id, state and city. '' is possible. return_values could be id, state or city"""

        # build filter
        search_for = {}
        if zipcode != "":
            search_for["_id"] = zipcode
        if state != "":
            search_for["state"] = state
        if city != "":
            search_for["city"] = city

        # get documents
        found_docs = []
        result = set()
        for post in Constants.COLLECTION.find(search_for):
            found_docs.append(post)
            if Constants.VERBOSE:
                print("FOUND: " + str(post))
            # select
            if selected == 'zip':
                result.add(post['_id'])
            elif selected == 'state':
                result.add(post['state'])
            elif selected == 'city':
                result.add(post['city'])

        return result
