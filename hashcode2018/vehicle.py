class Vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rides = []
        self.is_in_use = False

    def distance_to_ride(self, ride):
        return abs(self.x - ride.a) + abs(self.y - ride.b)

    def add_ride(self, r):
        self.rides.append(r)
        self.is_in_use = True

    def get_output(self):
        s = str(len(self.rides))
        if len(self.rides) > 0:
            s += ' '
        s += ' '.join(str(ride.nr) for ride in self.rides)
        return s

    def try_to_end_ride(self, current_time):
        if not len(self.rides):
            return False
        last_ride = self.rides[-1]
        if last_ride.start_time + last_ride.distance == current_time:
            last_ride.end_time = current_time
            self.is_in_use = False
            self.x = last_ride.x
            self.y = last_ride.y

    def can_finish_ride(self, ride, current_time):
        if self.distance_to_ride(ride) + ride.distance + current_time < ride.f:
            return True
        # print "time: %s can't finish this ride: %s " % (current_time, ride)
        return False
