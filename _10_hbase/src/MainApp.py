import getopt as getOpt
import sys

from data_access.Constants import Constants
from data_access.Reader import Reader
from data_access.Saver import Saver


class MainApp:
    """Holds the main-method for command line"""

    def __init__(self):
        self.reader = Reader()
        self.saver = Saver()

    def main(self):
        """Reads command line options"""

        # Default values
        zipcode = ''
        state = ''
        city = ''
        selected = 'zipcode'
        file_to_save = 'plz.data'
        save = False
        read = False

        # parse command line options
        try:
            opts, args = getOpt.getopt(sys.argv[1:], "vhz:s:c:", ["help", "verbose", "zip=", "state=", "city=",
                                                                  "select=", "save=", "save", "clear"])
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
            elif o in ("-z", "--zip"):
                zipcode = a
                read = True
            elif o in ("-s", "--state"):
                state = a
                read = True
            elif o in ("-c", "--city"):
                city = a
                read = True
            elif o in "--select":
                selected = a
                read = True
            elif o in "--save":
                if a != '':
                    file_to_save = a
                save = True
            elif o in "--clear":
                self.saver.delete_all()
            else:
                assert False, "unhandled option"

        if save:
            count = self.saver.save_file_from_resource(file_to_save)
            print(str(count) + ' rows saved!')
        if read:
            for result in self.reader.find_and_select(zipcode, state, city, selected):
                print(result)

    @staticmethod
    def usage():
        print(
            "Usage: \n"
            "  - Saving:   Use --save <filename> to save a File from resource folder \n"
            "  - Reading:  Use [-i, --id] [-s, --state] [-c, --city] and --select <['id', 'state', 'city']> \n"
            "  - Deleting: Use --clear to delete all from database")


# Define main method
if __name__ == "__main__":
    MainApp().main()
