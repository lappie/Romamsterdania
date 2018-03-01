
def read_file(file_name):
    with open(file_name, "r") as f:
        pass
        # first_line = f.readline()
        # r, c, l, h = first_line.split()
        # r = int(r)
        # c = int(c)
        # l = int(l)
        # h = int(h)
        # matrix = [[0 for j in range(c)] for i in range(r)]
        # # print matrix
        # # print ("%s - %s - %s - %s" %(r,c,l,h))
        # for i in range(0, r):
        #     new_line = f.readline()
        #     for j in range(0, c):
        #         matrix[i][j] = new_line[j]
        # print matrix
    return "done"


def write_file(file_name, s, solution):
    with open("%s" % file_name, "w") as f:
        f.write("works \n")
        # for i in range(len(solution)):
        #     row = solution[i]
        #     f.write(row.toString())
        #     f.write("\n")