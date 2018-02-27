shape(min, max):
	shapes = []
	for i  in range(1,max)
		for j in range(1,max)
			if i*j>=min and i*j<=max:
				shapes.push([i,j])
	return shapes



checkShape(submatrix, min):
	sumM = 0
	sumT = 0
	for i in len(submatrix):
		for j in len(submatrix[0]):
			if submatrix[i][j] == 'M':
				sumM++
			elif submatrix[i][j] == 'T':
				sumT++
			else submatrix[i][j] == 's':
				return False
	if sumM>=min and sumT >= min:
		return True
	return False


getSubmatrix(matrix, idi, idj, idim, idjm)
	submatrix = []
	for i in range(idi, idim):
		for j in range(idj, idjm):
			submatrix[i][j] = matrix[i][j]
	return submatrix

replaceSubmatrix(matrix, idi, idj, idim, idjm):
	for i in range(idi, idim):
		for j in range(idj, idjm):
			matrix[i][j] = 's'
	return matrix

main():
	matrix = [1010101001010101010]
	result = [];
	min = 12
	max = 14
	shapes = shape(min,max)
	for i in range(1:1000):
		for j in range(1:1000):
			for k in shapes:
				submatrix = getSubmatrix(matrix, i, j, i+k[0], j+k[1])
				fits = checkShape(submatrix, min)
				if fits:
					matrix = replaceSubmatrix(matrix, i, j, i+k[0], j+k[1])
					result.push([i,j, i+k[0], j+k[1]])
					break
	
