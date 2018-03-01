from ride import Ride
from vehicle import Vehicle


def sort_compare_function(item1, item2):
    if item1.s < item2.s:
        return -1
    if item1.s == item2.s and item1.distance < item2.distance:
        return -1
    return 1


def select_ride_for_vehicle(rides, vehicle):
    pass


def greedy(rows, columns, cars, bonus,  T, rides):
    rides = sorted(rides, cmp=sort_compare_function)
    print rides
    for t in range(T):
        for vehicle in cars:
            vehicle.try_to_end_ride(t)
            if not vehicle.is_in_use:
                # get a ride
                if not len(rides):
                    break
                # select_ride_for_vehicle()
                vehicle.add_ride(rides.pop(0))
