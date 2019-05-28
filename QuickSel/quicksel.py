import numpy as np
import sys
import random
from sklearn.neighbors import NearestNeighbors
from hyper_rect_area import hyper_rect_area
from hyper_rects_intersection import hyper_rects_intersection

range_attr = [0, 23, 0, 30]
lamda = 100000

#Find n Bs for n queries
B = np.loadtxt("training_boxes.txt", delimiter=" ")
S = np.loadtxt("training_selectivities.txt")
n = np.size(B,0) #number of training boxes



# Randomly generate p points in each B
points = []
dim = 2 #number of attributes in the relation
p = 10 #number of points in each box
for i in range(n):
	for j in range(p):
		point = []
		for k in range(dim):
			point.append(random.uniform(B[i][k*2],B[i][k*2+1]))
		points.append(point)

# p=0
# for i in range(n):
# 	# p=10
# 	area = hyper_rect_area(B[i])
# 	if area<=3:
# 		p = 10
# 	else :
# 		p = 10*np.log(area)
# 	for j in range(int(np.around(p))):
# 		point = []
# 		for k in range(dim):
# 			point.append(random.uniform(B[i][k*2],B[i][k*2+1]))
# 		points.append(point)


# Out of 10*n points, sample m = min(4n,4000) points
m = min(2*n,2000)
random.shuffle(points)
points = points[:m]

# Make m Gs for m points
nbrs = NearestNeighbors(n_neighbors=31, algorithm='ball_tree').fit(points)
distances, indices = nbrs.kneighbors(points)
# print(indices)



#Creating Gs
G = []
for i in range(np.size(indices,0)):
	G_box = []
	for j in range(dim):
		G_box.append(float("inf"))
		G_box.append(float("-inf"))
	for j in range(1,np.size(indices,1)):
		for k in range(dim):
			attr_val = points[indices[i][j]][k]
			center_val = points[indices[i][0]][k]
			if attr_val > center_val:
				G_box[k*2] = min(G_box[k*2],2*center_val - attr_val)
				G_box[k*2+1] = max(G_box[k*2+1],attr_val)
			else :
				G_box[k*2] = min(G_box[k*2],attr_val)
				G_box[k*2+1] = max(G_box[k*2+1],2*center_val - attr_val)
			if G_box[k*2+1]<G_box[k*2]:
				print(center_val,attr_val)
	G.append(G_box)
# print(G)

for i in range(np.size(G,0)):
	for j in range(dim):
		G[i][j*2] = max(G[i][j*2],range_attr[j*2])
		G[i][j*2+1] = min(G[i][j*2+1],range_attr[j*2+1])
# print(G)


# Find area of Gs
area_G = []
for i in range(m):
	area_G.append(hyper_rect_area(G[i]))

np.savetxt("G.txt",G,delimiter=" ")
np.savetxt("area_G.txt",area_G,delimiter=" ")



# Find Q
Q = []
for i in range(m):
	temp = []
	for j in range(m):
		temp.append(hyper_rects_intersection(G[i],G[j])/area_G[i]/area_G[j])
	Q.append(temp)

np.savetxt("Q.txt",Q,delimiter=" ")

# Find A
A = []
for i in range(n):
	temp = []
	for j in range(m):
		temp.append(hyper_rects_intersection(B[i],G[j])/area_G[j])
	A.append(temp)

np.savetxt("A.txt",A,delimiter=" ")

# print(Q)
# print(A)


# Find W
Q = np.array(Q)
A = np.array(A)
W = A.transpose()
W = np.dot(W,A)
W = np.dot(lamda,W)
W = np.add(Q,W)
W = np.linalg.pinv(W)
W = np.dot(lamda,W)
W = np.dot(W,np.transpose(A))
W = np.dot(W,S)
W = np.dot(W,1/3214874)

np.savetxt("W.txt",W,delimiter=" ")