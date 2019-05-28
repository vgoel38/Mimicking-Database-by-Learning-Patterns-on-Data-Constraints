import numpy as np
import sys
import random

def training_test_generator():
	#Find n Bs for n queries
	B = np.loadtxt("dataset1200.csv", delimiter=" ")
	S = np.loadtxt("card1200.csv")
	n = np.size(B,0) #number of training boxes

	B_combined = []
	for i in range(np.size(B,0)):
		B_combined.append([*B[i],S[i]])
	B_combined = np.array(B_combined)
	B_combined = np.random.permutation(B_combined)

	S = B_combined[:,np.size(B_combined,1)-1]
	B = B_combined[:,:np.size(B_combined,1)-1]

	# B_train = B[:800]
	# S_train = S[:800]
	# B_test = B[801:]
	# S_test = S[801:]

	x = int(0.7*np.size(B_combined,0))

	B_train = B[:x]
	S_train = S[:x]
	B_test = B[x+1:]
	S_test = S[x+1:]

	np.savetxt("training_boxes.txt",B_train,delimiter=" ")
	np.savetxt("training_selectivities.txt",S_train,delimiter=" ")
	np.savetxt("test_boxes.txt",B_test,delimiter=" ")
	np.savetxt("test_selectivities.txt",S_test,delimiter=" ")

if __name__ == "__main__":
	training_test_generator()
