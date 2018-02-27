r, c, l, h, matrix = 0, 0, 0, 0, []


def read_file(file_name):
    global r, c, l, h, matrix
    with open(file_name, "r") as f:
        first_line = f.readline()
        r, c, l, h = first_line.split()
        r = int(r)
        c = int(c)
        l = int(l)
        h = int(h)
        matrix = [[0 for j in range(c)] for i in range(r)]
        # print matrix
        # print ("%s - %s - %s - %s" %(r,c,l,h))
        for i in range(0, r):
            new_line = f.readline()
            for j in range(0, c):
                matrix[i][j] = new_line[j]
        # print matrix
    return l, h, matrix


def write_file(file_name, s, solution):
    with open(file_name, "w") as f:
        f.write("%s\n" % s)
        for i in range(len(solution)):
            row = solution[i]
            for j in range(len(row)):
                f.write("%s " % row[j])
            f.write("\n")


def main():
    read_file("./small.in")
    write_file("./output.out", 3, [[0, 0, 1,2], [4,5,6,1], [7,7,8,8]])


if __name__ == '__main__':
    main()