import numpy as np
from PIL import Image
from Matrices import dot, add, divide, mult, subtract
from aireg import sigmoid, find_gradient, neighbors_simple
"""
Simple 2 layer 4 neuron network
"""
class SimpleNeural:
	def __init__(self, set_inputs, set_outputs):
		self.inputs = set_inputs
		self.layer1 = [] #3D array. Layers > Weight matrices > values. 
		for i in range(0, 4):
			self.layer1.append(np.random.random_sample(len(set_inputs[0])))
		self.layer2 = np.random.random_sample(4)
		self.outputs = set_outputs

	def feed_forward(self):
		output = []
		for article in self.inputs:
			next_part = []
			for i in range(0, 4):
				next_part.append(sigmoid(dot(self.layer1[i], article)))
			output.append(sigmoid(dot(next_part, self.layer2)))
		return output

	def loss(self):
		calculated = self.feed_forward()
		loss = 0
		for i in range(0, len(self.outputs)):
			loss += (self.outputs[i] + calculated[i])**2
		return loss

	def get_raw_parameters(self):
		parameters = []
		for arr in self.layer1:
			for num in arr:
				parameters.append(num)
		for num in self.layer2:
			parameters.append(num)
		return parameters

	def set_raw_parameters(self, parameters):
		counter = 0
		for i in range(0, len(self.layer1)):
			for j in range(0, len(self.layer1[i])):
				self.layer1[i][j] = parameters[counter]
				counter += 1
		for i in range(0, len(self.layer2)):
			self.layer2[i] = parameters[counter]
		return

	def train(self, times):
		print "initial loss"
		print self.loss()
		print "training..."
		start = self.get_raw_parameters()[::]
		for i in range(0,times):
			value = self.loss()
			print "enumerating neighbors"
			neighbors = neighbors_simple(start, .1)
			answers = []
			print "evaluating neighbors"
			for neighbor in neighbors:
				print "done"
				self.set_raw_parameters(neighbor)
				answers.append(self.loss() - value)
			print "finding gradient"
			gradient = find_gradient(neighbors, answers)
			start = subtract(start, gradient)
			self.set_raw_parameters(start)
			print "new loss"
			print self.loss()
		f = open("bots.txt", "a")
		f.write("\nNEWBOT")
		f.write(str(self.get_raw_parameters()))

def process_clothes():
	img = Image.open('resources\clothes.png').convert('L')
	img.save('resources\greyscale.png')
	arr = np.asarray(img)

	images = []
	for i in range(0, 840, 28):
		for j in range(0, 840, 28):
			image = []
			for row in arr[i: i + 28]:
				new_row = []
				for k in range(j, j + 28):
					new_row.append(row[k])
				image.append(new_row)
			images.append(image)
	pixelgroups = []
	for image in images:
		pixels = []
		for row in image:
			for pixel in row:
				pixels.append(pixel)
		pixelgroups.append(pixels)
	return pixelgroups

def main():
	answers = np.zeros(900)
	for i in range(30, 60):
		answers[i] = 1
	pants = SimpleNeural(process_clothes(),answers)
	pants.train(2)

if __name__ == "__main__":
	main()