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

    def simple2(self):
        i = 0
        myRides = copy.copy(self.rides)
        for i in range(len(self.vehicles)):
            ride = self.rides[i]
            self.vehicles[i].add_ride(ride)
            myRides.remove(ride)

        # Go to see for next pick_ups
        for i in range(len(self.vehicles)):
            vehicle = self.vehicles[i]
            available_time = vehicle.get_available_time()
            best_rides = [ride for ride in myRides if ride.s > available_time +
                          distance(vehicle.get_last_x(), vehicle.get_last_y(), ride.a, ride.b)]
            if len(best_rides) > 0:
                ride = best_rides[0]
                vehicle.add_ride(ride)
                myRides.remove(ride)

        return self.vehicles




