import numpy as np
import sys
from hyper_rect_area import hyper_rect_area



def hyper_rects_intersection(box1, box2):
	box = []
	for i in range(np.size(box1)):
		if i%2 == 0:
			if box1[i]>=box2[i+1] or box2[i]>=box1[i+1]:
				return 0
			else:
				box.append(max(box1[i],box2[i]))
				box.append(min(box1[i+1],box2[i+1]))
	return hyper_rect_area(box)



if __name__ == "__main__":
	print(hyper_rects_intersection([1,5,2,6,1,2],[2,4,3,8,1,2]))