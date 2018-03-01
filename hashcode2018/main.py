from read_write_function import read_file, write_file
from datetime import datetime

from simple import Simple
from vehicle import Vehicle

# a_example b_should_be_easy c_no_hurry d_metropolis e_high_bonus
INPUT_FILE = "e_high_bonus"


def main():
    start = datetime.now()
    # Rows, Columns, Vehicles, Rides, Bonus, Max Time
    R, C, F, N, B, T, rides = read_file('./input/' + INPUT_FILE + '.in')

    # Start solution here:
    vehicles = [Vehicle() for i in range(F)]
    simple = Simple(rides, vehicles)
    vehicles = simple.simple()

    now = datetime.now()
    write_file("./output/" + INPUT_FILE + " - " + str(now.hour) + 'h' + str(now.minute) + 'm' +
               str(now.second) + "s.out", vehicles)
    print 'runtime: ' + str(datetime.now()-start)


if __name__ == '__main__':
    main()
