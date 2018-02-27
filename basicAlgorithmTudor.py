import main

def shape(min, max):
    shapes = []
    for i in range(1,max+1):
        for j in range(1,max+1):
            if i*j>=min*2 and i*j<=max:
                shapes.append([i, j])
    return shapes



def checkShape(submatrix, min):
    sumM = 0
    sumT = 0
    for i in range(len(submatrix)):
        for j in range(len(submatrix[0])):
            if submatrix[i][j] == 'M':
                sumM+=1
            elif submatrix[i][j] == 'T':
                sumT+=1
            else:
                return False
    if sumM>=min and sumT >= min:
        return True
    return False


def getSubmatrix(matrix, idi, idj, idim, idjm):
    submatrix = [['' for j in range(idjm)] for i in range(idim)]
    if idi+idim>len(matrix):
        return False
    if idj+idjm>len(matrix[0]):
        return False
    for i in range(idi, idi+idim):
        for j in range(idj, idj+idjm):
            submatrix[i][j] = matrix[i][j]
    return submatrix

def replaceSubmatrix(matrix, idi, idj, idim, idjm):
    for i in range(idi, idim):
        for j in range(idj, idjm):
            matrix[i][j] = 's'
    return matrix

def main2():
    min, max, matrix = main.read_file('small.in')
    result = []
    # print matrix
    shapes = shape(min, max)
    print shapes
    for i in range(0,999):
        for j in range(0,999):
            for k in shapes:
                submatrix = getSubmatrix(matrix, i, j, k[0], k[1])
                if submatrix:
                    print submatrix
                    fits = checkShape(submatrix, min)
                    if fits:
                        matrix = replaceSubmatrix(matrix, i, j, i+k[0], j+k[1])
                        print [i,j, i+k[0]-1, j+k[1]-1]
                        result.append([i,j, i+k[0], j+k[1]])
                        break
	

if __name__ == '__main__':
    main2()