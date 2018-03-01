from main import read_file


class Shape:
    def __init__(self, width, height, deviation_height, deviation_width):
        self.width = width
        self.height = height
        self.deviation_height = deviation_height
        self.deviation_width = deviation_width

    def get_shape_score(self):
        return self.width*self.height

    def __unicode__(self):
        return "%s x %s; deviation: %s x %s " % (self.height, self.width, self.deviation_height, self.deviation_width)


def get_shapes(L, H):
    shapes = []
    for i in range(1, H+1):
        for j in range(1, H+1):
            if i*j >= L*2 and i * j <= H:
                shapes.append([i, j])
    return shapes


def get_shapes_with_deviation(shapes):
    shapes_with_deviation = []
    for a_shape in shapes:
        height, width = a_shape
        for i in range(-height+1, 1):
            for j in range(-width+1, 1):
                shapes_with_deviation.append(Shape(width, height, i, j))
    return shapes_with_deviation


def shapes_fits(matrix, a_shape, l, matrix_i , matrix_j):
    try:
        no_mushrooms = 0
        no_tomatos = 0
        for i in range(a_shape.height):
            for j in range(a_shape.width):
                i_index = matrix_i + i + a_shape.deviation_height
                j_index = matrix_j + j + a_shape.deviation_width
                if matrix[i_index][j_index] == 'M':
                    no_mushrooms += 1
                else:
                    no_tomatos += 1
        if no_mushrooms >= l and no_tomatos >= l:
            return True
    except IndexError:
        pass
    return False


def init_score_matrix(c, r):
    return [[0 for j in range(c)] for i in range(r)]


def main_alg():
    r, c, l, h, matrix = read_file('./pizza/example.in')
    shapes = get_shapes(l, h)
    shapes_with_deviation = get_shapes_with_deviation(shapes)
    print len(shapes_with_deviation)
    for a_shape in shapes_with_deviation:
        print a_shape.__unicode__()
    score_matrix = init_score_matrix(c, r)
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            for a_shape in shapes_with_deviation:
                if shapes_fits(matrix, a_shape, l, i, j):
                    score_matrix[i][j] += 1
    print score_matrix

if __name__ == '__main__':
    main_alg()