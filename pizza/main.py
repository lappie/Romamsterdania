r, c, l, h, matrix = 0, 0, 0, 0, []
import magic

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
            f.write(row.toString())
            '''
            for j in range(len(row)):
                f.write("%s " % row[j])'''
            f.write("\n")


def main():
    f = "example"
    read_file("./input/" + f + ".in")
    m = magic.Magic(r, c, l, h, matrix)
    m.createShapes()
    m.printShapes()

    m.createGrid()
    #m.greedy()
    #m.printResults()
    #m.printGrid()
    m.printScore()

    m.createOptions()
    m.findOptions()
    m.printOptions()
    
    write_file("./output/" + f + ".out", len(m.results), m.results)


if __name__ == '__main__':
    main()
