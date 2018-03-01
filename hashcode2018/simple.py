import copy
from util import distance


class Simple:
    def __init__(self, rides, vehicles):
        self.rides = rides
        self.vehicles = vehicles

    # Just place first ride on first vehicle, no more
    def simple(self):
        for i in range(len(self.vehicles)):
            self.vehicles[i].add_ride(self.rides[i])
        return self.vehicles

    def filter_impossible_rides(self, rides, posX, posY, current_time):
        return [ride for ride in rides if ride.f - current_time > distance(ride.a, ride.b, posX, posY) + ride.distance]

    def sorted_rides(self, rides):
        rides.sort(key=lambda ride: distance(ride.x, ride.y, 0, 0))
        return rides

    def simple3(self, B, T):
        # first ones are clear:
        myRides = copy.copy(self.rides)
        myRides.sort(key=lambda ride : ride.getScore(B, T, 0, 0, 0))

        for vehicle in self.vehicles:
            vehicle.add_ride(myRides.pop())

        #
        change = True
        while change:
            change = False
            for vehicle in self.vehicles:
                myRides.sort(key=lambda ride: ride.getScore(B, T, vehicle.get_last_x(), vehicle.get_last_y(), vehicle.get_available_time()))
                if len(myRides) > 0: # and myRides[0].getScore(B, vehicle.get_last_x(), vehicle.get_last_y(), vehicle.get_available_time()):
                    vehicle.add_ride(myRides.pop())
                    change = True


        for i in range(len(self.vehicles)):
            vehicle = self.vehicles[i]
            available_time = vehicle.get_available_time()
            best_rides = self.filter_impossible_rides(myRides, vehicle.get_last_x(), vehicle.get_last_y(),
                                                      available_time)
            if len(best_rides) > 0:
                best_rides.sort(key=lambda ride: distance(ride.x, ride.y, 0, 0))
                ride = best_rides[0]
                vehicle.add_ride(ride)
                myRides.remove(ride)
                print(len(myRides))

        return self.vehicles



    def simple2(self):
        myRides = copy.copy(self.rides)
        self.sorted_rides(myRides)
        myRides = self.filter_impossible_rides(myRides, 0, 0, 0)
        myRides2 = copy.copy(myRides)

        # First round just assign something to everything
        for i in range(len(self.vehicles)):
            if len(myRides2) > i:
                ride = myRides2[i]
                self.vehicles[i].add_ride(ride)
                myRides.remove(ride)

        # Go to see for next pick_ups
        while True:
            change = True
            while change:
                change = False
                for i in range(len(self.vehicles)):
                    vehicle = self.vehicles[i]
                    available_time = vehicle.get_available_time()
                    best_rides = [ride for ride in myRides if ride.s > available_time +
                                  distance(vehicle.get_last_x(), vehicle.get_last_y(), ride.a, ride.b)]
                    best_rides = self.filter_impossible_rides(best_rides, vehicle.get_last_x(), vehicle.get_last_y(), available_time)
                    if len(best_rides) > 0:
                        best_rides.sort(key=lambda ride: distance(ride.x, ride.y, 0, 0))
                        ride = best_rides[0]
                        vehicle.add_ride(ride)
                        myRides.remove(ride)
                        change = True

            # Go through everything without bonus
            change = False
            for i in range(len(self.vehicles)):
                vehicle = self.vehicles[i]
                available_time = vehicle.get_available_time()
                best_rides = self.filter_impossible_rides(myRides, vehicle.get_last_x(), vehicle.get_last_y(), available_time)
                if len(best_rides) > 0:
                    best_rides.sort(key=lambda ride: distance(ride.x, ride.y, 0, 0))
                    ride = best_rides[0]
                    vehicle.add_ride(ride)
                    myRides.remove(ride)
                    change = True
            if not change:
                return self.vehicles




