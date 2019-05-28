import sys
import numpy as np
from hyper_rect_area import hyper_rect_area
from hyper_rects_intersection import hyper_rects_intersection

B = np.loadtxt("training_boxes.txt", delimiter=" ")
S = np.loadtxt("training_selectivities.txt")
G = np.loadtxt("G.txt", delimiter=" ")
area_G = np.loadtxt("area_G.txt")
W = np.loadtxt("W.txt")

m = np.size(G,0)

S_predict = []

for i in range(np.size(B,0)):
	temp = []
	for j in range(m):
		val = hyper_rects_intersection(G[j],B[i])/area_G[j]
		temp.append(val)
		if np.isnan(val):
			print(hyper_rects_intersection(G[j],B[i]), area_G[j], j)
	temp = np.array(temp)
	S_predict.append(np.dot(W,temp))
	# if np.dot(W,temp) == 0:
		# print(i)

S_predict = np.array(S_predict)
S_predict = np.dot(3214874,S_predict)
S = S.astype(int)
S_predict = S_predict.astype(int)
S_predict = np.vstack((S, S_predict)).T

sys.stdout = open("predictions.txt",'w')
for val in S_predict:
	print(*abs(val))

sys.stdout = sys.__stdout__

rel_error = 0
for i in range(np.size(S_predict,0)):
	if S_predict[i][1] !=0 :
		rel_error = rel_error + abs(abs(S_predict[i][0]) - abs(S_predict[i][1]))/max(S_predict[i][0],abs(S_predict[i][1]))
		# print(rel_error, abs(S_predict[i][0]), abs(S_predict[i][1]))
# print(np.size(S_predict,0))
rel_error = rel_error/np.size(S_predict,0)
rel_error = rel_error*100

print(rel_error)

# np.savetxt("predictions.txt",S_predict.astype(int),delimiter=" ")