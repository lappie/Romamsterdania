import copy
from util import distance


class Simple:
    def __init__(self, rides, vehicles):
        self.rides = rides
        self.vehicles = vehicles

    def simple(self):
        for i in range(len(self.vehicles)):
            self.vehicles[i].add_ride(self.rides[i])
        return self.vehicles

    def sorted_rides(self):
        self.rides.sort(key=lambda ride: distance(ride.x, ride.y, 0, 0))

    def simple2(self):
        self.sorted_rides()
        i = 0
        myRides = copy.copy(self.rides)

        # First round just assign something to everything
        for i in range(len(self.vehicles)):
            ride = self.rides[i]
            self.vehicles[i].add_ride(ride)
            myRides.remove(ride)

        # Go to see for next pick_ups
        change = True
        while change:
            change = False
            for i in range(len(self.vehicles)):
                vehicle = self.vehicles[i]
                available_time = vehicle.get_available_time()
                best_rides = [ride for ride in myRides if ride.s > available_time +
                              distance(vehicle.get_last_x(), vehicle.get_last_y(), ride.a, ride.b)]
                if len(best_rides) > 0:
                    best_rides.sort(key=lambda ride: distance(ride.x, ride.y, 0, 0))
                    ride = best_rides[0]
                    vehicle.add_ride(ride)
                    myRides.remove(ride)
                    change = True

        return self.vehicles




