from Matrices import dot, add, subtract, mult, divide, rref, vector_projection, space_projection
from math import exp

"""
OLD 2D NEIGHBORS BY CIRCLE
from math import cos, sin, pi
def neighbors2D(pos, dist):
	neighbors = []
	new_pos = []
	for coord in pos:
		new_pos.append(float(coord))
	for i in range(0,36):
		angle = 2 * pi * (i / 36.)
		unit = [dist * cos(angle), dist * sin(angle)]
		neighbor = add(new_pos, unit)
		neighbors.append(neighbor)
	return neighbors
"""
def sigmoid(x):
	return 1. / (1 + exp(-x))

def cartesian_product(lists):
	final_product = []
	if len(lists) == 1:
		list_objects = []
		for obj in lists[0]:
			list_objects.append([obj])
		return list_objects
	product = cartesian_product(lists[1::])
	for i in lists[0]:
		for j in range(0, len(product)):
			combination = product[j][::]
			combination.append(i)
			final_product.append(combination)
	for combination in final_product:
		combination = combination.reverse()
	return final_product

def neighbors_cartesian(pos, dist):
	neighbors = []
	new_pos = []
	variations = []
	dist = float(dist)
	for coord in pos:
		new_pos.append(float(coord))
		variations.append([-dist, 0, dist])
	variations = cartesian_product(variations)
	for variation in variations:
		is_null = True
		for i in variation:
			if i != 0:
				is_null = False
		if is_null:
			continue
		neighbors.append(add(variation, new_pos))
	return neighbors

def neighbors_simple(pos, dist):
	neighbors = []
	new_pos = []
	dist = float(dist)
	for coord in pos:
		new_pos.append(float(coord))
	for i in range(0,len(pos)):
		positive = new_pos[::]
		positive[i] = positive[i] + dist
		negative = new_pos[::]
		negative[i] = negative[i] - dist
		neighbors.append(positive)
		neighbors.append(negative)
	return neighbors

def find_gradient(input_mat, answers):
	vectors = []
	for i in range(0, len(input_mat[0])):
		column = []
		for j in range(0, len(input_mat)):
			column.append(input_mat[j][i])
		vectors.append(column)
	target = space_projection(answers, vectors)
	for i in range(0, len(input_mat)):
		input_mat[i].append(target[i])
	gradient = []
	#for equation in rref(input_mat[dimdiff::]):
	#	gradient.append(equation[-1])

	LISys = [input_mat[0]]
	for i in range(1, len(input_mat)):
		LITest = LISys[::]
		LITest.append(input_mat[i])
		if is_blank(rref(LITest)[-1]):
			continue
		LISys.append(input_mat[i])
		if len(LISys) >= len(input_mat[0]) - 1:
			break
#		print_mat(LISys)
	LISys = rref(LISys)
	for equation in LISys:
		gradient.append(equation[-1])
	return gradient

def is_blank(vector):
	for element in vector:
		if abs(element) > .0001:
			return False
	return True

"""
TEST FUNCTIONS FOR OPTIMIZATION

def f2(l):
	x = l[0]
	y = l[1]
	return g(x,y)

def f3(l):
	x = l[0]
	y = l[1]
	z = l[2]
	return (- x**2 - 3 * (y + 2)**2 - 4 * (z - 7)**2)

def g(x, y):
	return (- x**2 - 3 * (y + 2)**2)

def f12(l):
	return f3(l[0:3]) + f2(l[3:5]) + f2(l[5:7]) + f3(l[7:10]) + f2(l[10:12])
"""

"""
#TEST SCRIPT FOR FUNCTIONS

start = [-6,-43,4,3,7,9,13,44,3,-42,-5,-90]
stepsize = .01

for unused in range(0, 1000):
	value = f12(start)
	neighbors = neighbors_simple(start, stepsize)
	answers = []
	for neighbor in neighbors:
		answers.append(f12(neighbor))
	for i in range(0, len(neighbors)):
		neighbors[i] = subtract(neighbors[i], start)
	for i in range(0, len(answers)):
		answers[i] -= value
#	for i in range(0, len(neighbors)):
#		print neighbors[i], answers[i]
	step = mult(stepsize, find_gradient(neighbors, answers))
	start = add(start, step)

print start
"""