import math

class Part:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def toString(self):
        return str(self.y1) + " " + str(self.x1) + " " + str(self.y2) + " " + str(self.x2)

    def getScore(self):
        return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1)
        
class Shape:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def getScore(self):
        return w*h

    def viceVersa(self):
        return Shape(self.h, self.w)

    def isValid(self, minIngredients, maxParts):
        if self.w*self.h < 2*minIngredients:
            return False
        if self.w*self.h > maxParts:
            return False
        return True

    def toString(self):
        return str(self.w) + "x" + str(self.h)


class Magic:
    shapes = []
    grid = []

    results = []

    def __init__(self, R, C, minIngredients, maxParts, matrix):
        self.R = R
        self.C = C
        self.minIngredients = minIngredients
        self.maxParts = maxParts
        self.matrix = matrix

    def createShapes(self):
        self.shapes = []
        root = int(math.floor(math.sqrt(self.maxParts)))
        for i in range(self.maxParts, root-1, -1):
            for j in range(1, root+1):
                s = Shape(i, j)
                if s.isValid(self.minIngredients, self.maxParts):
                    self.shapes.append(s)
        #Put the vice versa's also here:
        length = len(self.shapes)
        for i in range(length):
            s = self.shapes[i]
            if s.w != s.h:
                self.shapes.append(s.viceVersa())

    def printShapes(self):
        print("Shapes:")
        for s in self.shapes:
            print(s.toString())
        print

    def createGrid(self):
        self.grid = [[True] * self.C for r in range(self.R)]

    def fits(self, shape, x, y):
        if x + shape.w > self.C:
            return False
        if y + shape.h > self.R:
            return False
        for h in range(shape.h):
            for w in range(shape.w):
                if not self.grid[y + h][x + w]:
                    return False
        return True

    def place(self, shape, x, y):
        #print("placing: " + shape.toString())
        for h in range(shape.h):
            for w in range(shape.w):
                self.grid[y + h][x + w] = False

    #does it contain minimum ingredients
    def valid(self, shape, x, y):
        l = ""
        for h in range(shape.h):
            for w in range(shape.w):
                l += self.matrix[y + h][x + w]
        if l.count('T') < self.minIngredients or l.count('M') < self.minIngredients:
            #print(l)
            return False
        return True

    def addResult(self, shape, x, y):
        p = Part(x, y, x+shape.w-1, y+shape.h-1)
        self.results.append(p)

    def greedy(self):
        for y in range(self.R):
            for x in range(self.C):
                if self.grid[y][x]:
                    for s in self.shapes:
                        if self.fits(s, x, y):
                            if self.valid(s, x, y):
                                self.place(s, x, y) 
                                self.addResult(s, x, y)
                                #break: optimize here, break the for loop

    def printResults(self):
        print("Results: ")
        for r in self.results:
            print(r.toString())
        print

    def printGrid(self):
        print("Grid:")
        print(self.grid)

    def printScore(self):
        s = 0
        for r in self.results:
            s += r.getScore()
        print("SCORE: " + str(s))
        
'''
m = Magic(5,4, 1, 3)
m.createShapes()
m.printShapes()

m.createGrid()
m.greedy()
m.printResults()
m.printGrid()
'''
