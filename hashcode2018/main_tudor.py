from read_write_function import read_file, write_file

def doGoogle(input_data):
    print input_data
    out = input_data
    return out





def main():
    input_data = read_file('./input/input.txt')
    out = doGoogle(input_data)
    write_file("testing.out", "", [])

if __name__ == '__main__':
    main()
