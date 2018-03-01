class Vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rides = []
        self.is_in_use = False

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


