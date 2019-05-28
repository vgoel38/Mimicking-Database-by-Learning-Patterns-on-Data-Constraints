import numpy as np
import sys
import random

def training_test_generator():
	#Find n Bs for n queries
	B = np.loadtxt("jobdataset.txt", delimiter=" ")
	S = np.loadtxt("jobcard.txt")
	n = np.size(B,0) #number of training boxes

	B_train = B[:15000]
	S_train = S[:15000]
	B_test = B[15001:]
	S_test = S[15001:]

	np.savetxt("training_boxes.txt",B_train,delimiter=" ")
	np.savetxt("training_selectivities.txt",S_train,delimiter=" ")
	np.savetxt("test_boxes.txt",B_test,delimiter=" ")
	np.savetxt("test_selectivities.txt",S_test,delimiter=" ")

if __name__ == "__main__":
	training_test_generator()
