from ride import Ride


def read_file(file_name):
    rides = []
    with open(file_name, "r") as file:
        first_line = file.readline()
        R, C, F, N, B, T = first_line.split()
        R = int(R)
        C = int(C)
        F = int(F)
        N = int(N)
        B = int(B)
        T = int(T)
        # print matrix
        # print ("%s - %s - %s - %s" %(r,c,l,h))
        for nr in range(0, R):
            ride_line = file.readline()
            if len(ride_line) > 0:
                a, b, x, y, s, f = ride_line.split()
                rides.append(Ride(int(a), int(b), int(x), int(y), int(s), int(f), nr))

        return R, C, F, N, B, T, rides


def write_file(file_name, vehicles):
    with open("%s" % file_name, "w") as f:
        for v in vehicles:
            if len(v.rides) > 0:
                f.write(v.get_output() + '\n')
        # for i in range(len(solution)):
        #     row = solution[i]
        #     f.write(row.toString())
        #     f.write("\n")