from ride import Ride
from vehicle import Vehicle


def sort_compare_function(item1, item2):
    if item1.s < item2.s:
        return -1
    if item1.s == item2.s and item1.distance < item2.distance:
        return -1
    return 1


def prepare_rides(rides, vehicle, current_time, bonus):
    #look at the next
    rides.sort(key=lambda a_ride: vehicle.distance_to_ride(a_ride) - bonus if vehicle.distance_to_ride(
        a_ride) + current_time < a_ride.f else vehicle.distance_to_ride(a_ride))
    return rides


def greedy(rows, columns, cars, bonus,  T, rides):
    rides = sorted(rides, cmp=sort_compare_function)
    max_wait_time = 10
    for t in range(T):
        for vehicle in cars:
            vehicle.try_to_end_ride(t)
            if not vehicle.is_in_use:
                # get a ride
                if not len(rides):
                    break
                # get sub-list of next rides

                # prepare_rides()
                for i in range(len(rides)):
                    if vehicle.can_finish_ride(rides[i], t):
                        vehicle.add_ride(rides.pop(0))
                        break
