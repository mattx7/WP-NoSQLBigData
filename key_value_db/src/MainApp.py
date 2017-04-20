import getopt as getOpt
import sys

sys.path.append("/home/lionpierau/projects/pycharm/NoSQL/")

from key_value_db.src.data_access.Reader import Reader
from key_value_db.src.data_access.Constants import Constants
from key_value_db.src.data_access.Saver import Saver


class MainApp:
    """Holds the main-method for command line"""

    def __init__(self):
        self.reader = Reader
        self.saver = Saver

    def main(self):
        """Reads command line options"""
        # TODO SAVER über commandprompt
        # Default values
        id = ''
        state = ''
        city = ''
        return_value = 'id'

        # parse command line options
        try:
            opts, args = getOpt.getopt(sys.argv[1:], "vhi:s:c:r:",
                                       ["help", "verbose", "id=", "state=", "city=", "return="])
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
            elif o in ("-s", "--state"):
                state = a
            elif o in ("-c", "--city"):
                city = a
            elif o in ("-r", "--return"):
                return_value = a
            else:
                assert False, "unhandled option"
        for result in self.reader.filter_and_return(id, state, city, return_value):
            print(result)

    @staticmethod
    def usage():
        print(
            "Usage: Filter with [-i,--id] [-s,--state] [-c,--city] and [-r,--return] could be 'id', 'state' or 'city' ")


# Define main method
if __name__ == "__main__":
    MainApp().main()
