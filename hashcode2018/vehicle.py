class Vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rides = []

    def add_ride(self, r):
        self.rides.append[r]

    def get_output(self):
        s = str(len(self.rides))
        if len(self.rides) > 0:
            s += ' '
        s += ' '.join(str(ride.nr) for ride in self.rides)
        return s
