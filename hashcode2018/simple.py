

class Simple:
    def __init__(self, rides, vehicles):
        self.rides = rides
        self.vehicles = vehicles

    def simple(self):
        for i in range(len(self.vehicles)):
            self.vehicles[i].add_ride(self.rides[i])
        return self.vehicles
