from read_write_function import read_file, write_file
from datetime import datetime

from simple import Simple
from vehicle import Vehicle

# a_example b_should_be_easy c_no_hurry d_metropolis e_high_bonus
INPUT_FILES = 'a_example b_should_be_easy c_no_hurry d_metropolis e_high_bonus'.split()
INPUT_FILE = "b_should_be_easy"



def solve(file):
    start = datetime.now()

    # Rows, Columns, Vehicles, Rides, Bonus, Max Time
    R, C, F, N, B, T, rides = read_file('./input/' + file + '.in')
    vehicles = [Vehicle() for i in range(F)]

    # Start solution here:
    vehicles = [Vehicle() for i in range(F)]
    simple = Simple(rides, vehicles)
    vehicles = simple.simple2()

    now = datetime.now()
    write_file("./output/" + file + " - " + str(now.hour) + 'h' + str(now.minute) + 'm' +
               str(now.second) + "s.out", vehicles)
    print 'runtime: ' + str(datetime.now() - start)


def solve_all():
    print(INPUT_FILES)
    for file in INPUT_FILES:
        print("FILE: " + file)
        solve(file)


def main():
    #solve(INPUT_FILE)
    solve_all()


if __name__ == '__main__':
    main()
