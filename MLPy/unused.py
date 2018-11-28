import aireg
import json
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


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
print len(pixelgroups)


"""
for i in range(0, 840, 28):
	for j in range(0, 840, 28):
"""