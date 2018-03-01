from read_write_function import read_file, write_file


def main():
    print read_file('./input/input.txt')

    write_file("testing.out", "", [])

if __name__ == '__main__':
    main()
