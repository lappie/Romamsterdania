from read_write_function import read_file, write_file

def doGoogle(R, C, F, N, B, T, rides):
    print R, C, F, N, B, T
    rides = process_rides(rides)
    for ride in rides:
        print ride.d
    out = 1
    return out


def process_rides(rides):
    for ride in rides:
        ride.d = abs(ride.y-ride.b) + (ride.x-ride.a)
    return rides



def main():
    R, C, F, N, B, T, rides = read_file('./input/a_example.in')
    out = doGoogle(R, C, F, N, B, T, rides)
    write_file("testing.out", "", [])

if __name__ == '__main__':
    main()
