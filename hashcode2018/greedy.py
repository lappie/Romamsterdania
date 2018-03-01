from ride import Ride
from vehicle import Vehicle


def sort_compare_function(item1, item2):
    if item1.s < item2.s:
        return -1
    if item1.s == item2.s and item1.distance < item2.distance:
        return -1
    return 1


def prepare_rides(rides, vehicle, current_time):
    #look at the next
    rides.sort(key=lambda a_ride: a_ride.distance - vehicle.distance_to_ride(a_ride) if current_time > a_ride.s
                    else a_ride.distance - vehicle.distance_to_ride(a_ride) - (a_ride.s - current_time), reverse=True)
    return rides


def greedy(rows, columns, cars, bonus,  T, rides):
    rides = sorted(rides, cmp=sort_compare_function)
    for t in range(T):
        for vehicle in cars:
            vehicle.try_to_end_ride(t)
            if not vehicle.is_in_use:
                # get a ride
                if not len(rides):
                    break
                # get sub-list of next rides

                # last_change_to_catch_rides = [ride for ride in rides if t + vehicle.distance_to_ride() + ride.distance == ride.f]
                # sub_rides = rides[0: len(rides)/10] # first 10% of rides

                # sub_rides = [a_ride for a_ride in rides if (a_ride.f - t) < 100]
                # if not len(sub_rides):
                #     sub_rides = rides

                # try to re-order first rides based on how close they are to me
                rides.sort(key=lambda a_ride: vehicle.distance_to_ride(a_ride) if t > a_ride.s else vehicle.distance_to_ride(a_ride) + a_ride.s - t)

                # prepare_rides(rides[:100])
                for i in range(len(rides)):
                    if vehicle.can_finish_ride(rides[i], t):
                        vehicle.add_ride(rides.pop(i))
                        # vehicle.add_ride(sub_rides[i])
                        # rides.remove(sub_rides[i])
                        break
