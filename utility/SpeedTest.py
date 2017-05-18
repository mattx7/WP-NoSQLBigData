from _10_hbase.src import HBaseReader as Reader
from _10_hbase.src import HBaseSaver as Saver
from utility.Stopwatch import Stopwatch

keyStopwatch = Stopwatch()


def speed_test_save_clear(rounds):
    i = rounds
    print("\nStart save-clear test for key-value...")
    keyStopwatch.start()
    while i > 0:
        i -= 1
        Saver.delete_all()
        Saver.save_file("../resources/plz.data")
    display(rounds, keyStopwatch.stop())


def speed_test_find_by_id(rounds):
    startZip = 10000

    i = rounds
    zip = startZip
    print("\nStart find test by id  for key-value...")
    keyStopwatch.start()
    while i > 0:
        i -= 1
        zip += 1
        Reader.find_and_select(str(zip), "", "", "")
    display(rounds, keyStopwatch.stop())


def speed_test_find_by_city(rounds):
    i = rounds
    print("\nStart find test by city for key-value...")
    keyStopwatch.start()
    while i > 0:
        i -= 1
        Reader.find_and_select("", "", "HAMBURG", "")
    display(rounds, keyStopwatch.stop())


def display(rounds, time):
    print(str(rounds) + " rounds took " + str(time) + " seconds in average " + str(time / rounds))


# runSaveClearTest(1)
speed_test_find_by_id(250)
speed_test_find_by_city(250)
