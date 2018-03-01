from util import distance

class Ride:
    def __init__(self, a, b, x, y, s, f, nr):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f
        self.nr = nr  # This is the ride nr
        self.distance = abs(x-a) + abs(y-b)
        self.start_time = -1 # write was not started. Set to Ti value when it starts.
        self.end_time = -1

    def __repr__(self):
        return "\n(%s,%s) -> (%s-%s) start at %s , end by %s" % (self.a, self.b, self.x, self.y, self.s, self.f)

    def getScore(self, B, T, posX, posY, time):
        to = distance(posX, posY, self.a, self.b)
        if time + to + self.distance > T:
            return -999999
        bonus = 0
        if time + to < self.s:
            bonus = B
        wait_time = 0
        if time + to < self.s:
            wait_time = self.s - time - to

        plus = self.distance + bonus
        min = to + wait_time
        return plus - min

    def __eq__(self, other):
        return self.nr == other.nr

