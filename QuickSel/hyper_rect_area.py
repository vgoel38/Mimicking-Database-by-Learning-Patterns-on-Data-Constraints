import numpy as np
import sys

def hyper_rect_area(box):
	product = 1
	for i in range(np.size(box)):
		if i%2 == 0:
			product = product * (box[i+1]-box[i])
	return product