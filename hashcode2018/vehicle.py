from util import distance

class Vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rides = []

    def add_ride(self, r):
        self.rides.append(r)

    def get_output(self):
        s = str(len(self.rides))
        if len(self.rides) > 0:
            s += ' '
        s += ' '.join(str(ride.nr) for ride in self.rides)
        return s

    # what time is this vehicle available
    def get_available_time(self):
        time = 0
        prevX = 0
        prevY = 0
        for ride in self.rides:
            time += distance(prevX, prevY, ride.a, ride.b)
            time += distance(ride.a, ride.b, ride.x, ride.y)
            prevX = ride.x
            prevY = ride.y
        return time

    def get_last_x(self):
        if len(self.rides) == 0:
            return 0
        return self.rides[-1].x

    def get_last_y(self):
        if len(self.rides) == 0:
            return 0
        return self.rides[-1].y
