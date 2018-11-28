def print_mat(mat):
	for eq in mat:
		print eq
def dot(x,y):
	sum = 0.
	if len(x) != len(y):
		return
	for i in range(0,len(x)):
		sum += x[i] * y[i]
	return sum
def add(x,y): 
	new_list = []
	if len(x) != len(y):
		return
	for i in range(0,len(x)):
		new_list.append(x[i] + y[i])
	return new_list
def subtract(x,y):
	new_list = []
	if len(x) != len(y):
		return
	for i in range(0,len(x)):
		new_list.append(x[i] - y[i])
	return new_list
def mult(scalar, vector):
	scalar = float(scalar)
	new_vector = []
	for element in vector:
		new_vector.append(element * scalar)
	return new_vector
def divide(scalar, vector):
	scalar = 1/float(scalar)
	return mult(scalar, vector)
def rref(mat):
	for i in range(1, len(mat)):
		counter = 0
		while abs(mat[i][i]) <= .00001:
			temp = mat[i]
			mat[i] = mat[-1]
			mat[-1] = temp
			counter += 1
			if counter >= len(mat):
				return [[0]]
		for j in range(0, i):
			if abs(mat[j][j]) < .00001:
				continue
			multiplier = float(mat[i][j]) / mat[j][j]
			mat[i] = subtract(mat[i], mult(multiplier, mat[j]))
	for i in range(0, len(mat)):
		for j in range(i + 1, len(mat)):
			if abs(mat[j][j]) < .00001:
				continue
			multiplier = float(mat[i][j]) / mat[j][j]
			mat[i] = subtract(mat[i], mult(multiplier, mat[j]))
	for i in range(len(mat)):
		if abs(mat[i][i]) < .00001:
			continue
		mat[i] = divide(mat[i][i],mat[i])
	return mat

def vector_projection(x, y):
	floatx = []
	floaty = []
	for element in x:
		floatx.append(element)
	for element in y:
		floaty.append(element)
	scalar = dot(floatx,floaty)/dot(floaty,floaty)
	for i in range(0,len(floaty)):
		floaty[i] *= scalar
	return floaty
def mat_mult(x, y):
	new_mat = []
	for i in range(0,len[x]):
		new_row = []
		for j in range(0, len(y[0])):
			column_vector_y = []
			for k in range(0, len(y)):
				column_vector_y.append(y[k][j])
			new_row.append(dot(column_vector_y, x[i]))
		new_mat.append(new_row)
	return new_mat

def invert(mat):
	dim = len(mat)
	new_mat = []
	if len(mat) != len(mat[0]):
		return
	for i in range(0, len(mat)):
		new_row = []
		for element in mat[i]:
			new_row.append(element)
		for j in range(0, len(mat)):
			new_row.append(int(i == j))
		new_mat.append(new_row)
	new_mat = rref(new_mat)
	final_mat = []
	for row in new_mat:
		final_mat.append(row[dim::])
	return final_mat

def space_projection(vector, space):
	projection = []
	for i in range(1, len(space)):
		for j in range(0, i):
			space[i] = subtract(space[i], vector_projection(space[i], space[j]))
	for i in range(0, len(vector)):
		projection.append(0)
	for dimension in space:
		projection = add(projection, vector_projection(vector, dimension))
	return projection