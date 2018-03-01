from read_write_function import read_file, write_file
from datetime import datetime

# a_example b_should_be_easy c_no_hurry d_metropolis e_high_bonus
INPUT_FILE = "input"


def main():
    start = datetime.now()
    print read_file('./input/' + INPUT_FILE + '.txt')

    now = datetime.now()
    write_file("./output/" + INPUT_FILE + " - " + str(now.hour) + 'h' + str(now.minute) + 'm' +
               str(now.second) + "s.out", "", [])
    print 'runtime: ' + str(datetime.now()-start)


if __name__ == '__main__':
    main()
