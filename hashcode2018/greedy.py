from ride import Ride
from vehicle import Vehicle


def sort_compare_function(item1, item2):
    if item1.s < item2.s:
        return False
    if item1.s == item2.s:
        return item1.distance < item2.distance
    return True


def greedy(rows, columns, cars, bonus,  T, rides):
    sorted(reversed(rides), cmp=sort_compare_function)

    for t in range(T):
        for vehicle in cars:
            vehicle.try_to_end_ride(t)
            if not vehicle.is_in_use:
                # get a ride
                if not len(rides):
                    break
                vehicle.add_ride(rides.pop(0))
