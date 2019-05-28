import matplotlib.pyplot as plt
import sys
card_file_name = sys.argv[1]
est_card = list()
act_card = list()
with open(card_file_name,'r') as card_file_handler:
	for line in card_file_handler:
		card = line.split(' ')
		act_card.append(int(card[0]))
		est_card.append(int(card[1]))
#whole data
'''plt.plot(act_card,act_card,color='green')
plt.scatter(act_card, est_card, color='red',marker= '.')
plt.axis([0, max(act_card), 0, max(est_card)])
plt.xlabel('Actual Cardinalities')
plt.ylabel('Estimated Cardinalities')
plt.title('Actual vs Estimated Cardinalities (aka_title)')
plt.show()
'''
#cardinality range a to b
a=0
# b=10000
b = max(act_card)
act_card_plot = list()
est_card_plot = list()
for i in range(len(act_card)):
	if act_card[i] > a and act_card[i] <=b:
		# if abs(act_card[i]-est_card[i])>=200000 and min(act_card[i],est_card[i])<50000:
			# print(act_card[i],est_card[i])
		act_card_plot.append(act_card[i])
		est_card_plot.append(est_card[i])
plt.plot(act_card_plot,act_card_plot,color='green')
plt.scatter(act_card_plot, est_card_plot, color='red',marker= '.')
plt.axis([min(act_card_plot), max(act_card_plot), a, b])
# plt.axis([min(act_card_plot), max(act_card_plot), min(est_card_plot), max(est_card_plot)])
plt.xlabel('Actual Cardinalities')
plt.ylabel('Estimated Cardinalities')
plt.title('Actual vs Estimated Cardinalities (aka_title)')
plt.show()