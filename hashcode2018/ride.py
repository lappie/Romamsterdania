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

    def __repr__(self):
        return "\n(%s,%s) -> (%s-%s) start at %s , end by %s" % (self.a, self.b, self.x, self.y, self.s, self.f)