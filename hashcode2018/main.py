import main_tudor
from read_write_function import read_file, write_file


def main():
    input_data = read_file('./input/input.txt')
    print input_data
    out = main_tudor.main()
    write_file("testing.out", "", [])

if __name__ == '__main__':
    main()
