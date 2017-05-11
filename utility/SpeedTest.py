from _7_mongo_db.src.data_access.Reader import Reader as MReader
from _7_mongo_db.src.data_access.Saver import Saver as MSaver

from _04_key_value_db.src.data_access.Reader import Reader as KReader
from _04_key_value_db.src.data_access.Saver import Saver as KSaver
from utility.Stopwatch import Stopwatch

keyStopwatch = Stopwatch()
mongosStopwatch = Stopwatch()

keySaver = KSaver()
mongoSaver = MSaver()

keyReader = KReader()
mongoReader = MReader()


def runSaveClearTest(rounds):
    i = rounds
    print("Start save-clear test for key-value...")
    keyStopwatch.start()
    while i > 0:
        i = i - 1
        keySaver.delete_all()
        keySaver.save_file("../resources/plz.data")
    display(rounds, keyStopwatch.stop())

    i = rounds
    print("Start save-clear test for mongoDB...")
    keyStopwatch.start()
    while i > 0:
        i = i - 1
        mongoSaver.delete_all()
        mongoSaver.save_file("../resources/plz.data")
    display(rounds, keyStopwatch.stop())


def runFindTestById(rounds):
    startZip = 10000

    i = rounds
    zip = startZip
    print("Start find test by id  for key-value...")
    keyStopwatch.start()
    while i > 0:
        i = i - 1
        zip = zip + 1
        keyReader.filter_and_return(str(zip), "", "", "")
    display(rounds, keyStopwatch.stop())

    i = rounds
    zip = startZip
    print("Start find test by id for mongoDB...")
    keyStopwatch.start()
    while i > 0:
        i = i - 1
        zip = zip + 1
        mongoReader.find_and_select(str(zip), "", "", "")
    display(rounds, keyStopwatch.stop())


def runFindTestByCity(rounds):
    i = rounds
    print("Start find test by city for key-value...")
    keyStopwatch.start()
    while i > 0:
        i = i - 1
        keyReader.filter_and_return("", "", "HAMBURG", "")
    display(rounds, keyStopwatch.stop())

    i = rounds
    print("Start find test by city for mongoDB...")
    keyStopwatch.start()
    while i > 0:
        i = i - 1
        mongoReader.find_and_select("", "", "HAMBURG", "")
    display(rounds, keyStopwatch.stop())


def display(rounds, time):
    print(str(rounds) + " rounds took " + str(time) + " seconds in average " + str(time / rounds))


# runSaveClearTest(1)
runFindTestById(250)
runFindTestByCity(250)
