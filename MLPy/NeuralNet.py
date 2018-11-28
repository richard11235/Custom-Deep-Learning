import numpy as np
from Matrices import add, divide, mult, subtract
from aireg import sigmoid, find_gradient, neighbors_simple
class NeuralNet:
	#set_inputs: parsed array of greyscale pixels
	#set_outputs: set outputs
	#set_neurons: number of neurons per layer
	#set_layers: number of layers
	def __init__(self, set_inputs, set_outputs, set_neurons, set_layers): #inputs are numpy arrays
		self.inputs = set_inputs
		self.layers = [] #3D array. Layers > Weight matrices > values. 
		self.layers.append(np.random.random_sample(len(set_inputs[0]))) #First layer dependent on inputs
		self.biases = [] #2D array. Layers > biases.
		self.biases.append(np.random.random_sample(len(set_inputs[0])))
		for i in range(1, set_layers):
			self.layers.append(np.random.random_sample(set_neurons))
			self.layers.append(np.random.random_sample(set_neurons)) #Adding in other layers
		outputs = set_outputs

	def get_layer(index):
		return self.layers[index]

	def set_layer(new_layer, index):
		self.layers[index] = new_layer

	def feedforward(self):
		output = []
		for part in self.inputs:
			answers = part[::]
			answers = divide(float(255), answers)
			next_part = []
			for transformation in self.layers[0]:
				next_part.append()


def main():
	print "hi"
	
if __name__ == "__main__":
	main()