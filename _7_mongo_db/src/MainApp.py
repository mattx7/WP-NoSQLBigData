import getopt as getOpt
import sys

sys.path.append("/home/lionpierau/projects/pycharm/NoSQL/")

from _7_mongo_db.src.data_access.Reader import Reader
from _7_mongo_db.src.data_access.Constants import Constants
from _7_mongo_db.src.data_access.Saver import Saver


class MainApp:
    """Holds the main-method for command line"""

    def __init__(self):
        self.reader = Reader()
        self.saver = Saver()

    def main(self):
        """Reads command line options"""

        # Default values
        id = ''
        state = ''
        city = ''
        return_value = 'id'
        file_to_save = 'plz.data'
        save = False
        read = False

        # parse command line options
        try:
            opts, args = getOpt.getopt(sys.argv[1:], "vhi:s:c:r:",
                                       ["help", "verbose", "id=", "state=", "city=", "return=", "save=", "save",
                                        "clear"])
        except getOpt.GetoptError as err:
            print(str(err))  # will print something like "option -a not recognized"
            self.usage()
            sys.exit(2)

        # Only call with options
        if len(opts) == 0:
            self.usage()
            sys.exit(2)

        # process options
        for o, a in opts:
            if o in ("-h", "--help"):
                self.usage()
                sys.exit(0)
            elif o in ("-v", "--verbose"):
                Constants.VERBOSE = True
            elif o in ("-i", "--id"):
                id = a
                read = True
            elif o in ("-s", "--state"):
                state = a
                read = True
            elif o in ("-c", "--city"):
                city = a
                read = True
            elif o in ("-r", "--return"):
                return_value = a
                read = True
            elif o in "--save":
                if a != '':
                    file_to_save = a
                save = True
            else:
                assert False, "unhandled option"

        if save:
            count = self.saver.save_file_from_resource(file_to_save)
            print(str(count) + ' documents saved!')
        if read:
            for result in self.reader.filter_and_return(id, state, city, return_value):
                print(result)

    @staticmethod
    def usage():
        print(
            "Usage: \n"
            "  - Saving:   Use --save <filename> to save a File from resource folder \n"
            "  - Reading:  Use [-i, --id] [-s, --state] [-c, --city] and [-r, --return] <['id', 'state', 'city']> \n"
            "  - Deleting: Use --clear to delete all from database")


# Define main method
if __name__ == "__main__":
    MainApp().main()