import getopt as getOpt
import sys

import RedisConstants as Constants
import RedisReader as Reader
import RedisSaver as Saver


# sys.path.append(os.getcwd())


def main():
    """Reads command line options"""

    # Default values
    id = ''
    state = ''
    city = ''
    return_value = 'id'
    file_to_save = Constants.FILE_NAME
    save = False
    read = False

    # parse command line options
    try:
        opts, args = getOpt.getopt(sys.argv[1:], "vhz:s:c:r:",
                                   ["help", "verbose", "zip=", "state=", "city=", "select=", "save=", "save",
                                    "clear"])
    except getOpt.GetoptError as err:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    # Only call with options
    if len(opts) == 0:
        usage()
        sys.exit(2)

    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif o in ("-v", "--verbose"):
            Constants.VERBOSE = True
        elif o in ("-z", "--zip"):
            id = a
            read = True
        elif o in ("-s", "--state"):
            state = a
            read = True
        elif o in ("-c", "--city"):
            city = a
            read = True
        elif o in "--select":
            return_value = a
            read = True
        elif o in "--save":
            if a != '':
                file_to_save = a
            save = True
        elif o in "--clear":
            Saver.delete_all()
        else:
            assert False, "unhandled option"

    if save:
        count = Saver.save_file(file_to_save)
        print(str(count) + ' pairs saved!')
    if read:
        for result in Reader.filter_and_return(id, state, city, return_value):
            print(result)


def usage():
    print(
        "Usage: \n"
        "  - Saving:   Use --save <filename> to save a File from resource folder \n"
        "  - Reading:  Use [-i, --id] [-s, --state] [-c, --city] and --select ['id', 'state', 'city'] \n"
        "  - Deleting: Use --clear to delete all from database")


# Define main method
if __name__ == "__main__":
    main()
