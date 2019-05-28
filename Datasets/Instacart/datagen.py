import csv
import sys
import copy
import random



def warn(*args, **kwargs):
    pass

'''
fout = open('modifiedorders.csv','w')

with open('orders.csv') as fin:
	csv_reader = csv.reader(fin, delimiter=',')
	for line in csv_reader:
		if(line[6] != ''):
			fout.write(line[0])
			for index in range(1,len(line)):
				fout.write("," + line[index])
			fout.write('\n')
'''


col1_name = 'order_hour_of_day'
col2_name = 'days_since_prior_order'
col1 = []
col2 = []
col1_temp = []
col2_temp = []
tot_count = 0

with open('modifiedorders.csv') as fin:
    csv_reader = csv.reader(fin, delimiter=',')
    for line in csv_reader:
        if(len(line) < 7):
            continue
        col1.append(float(line[5]))
        col2.append(float(line[6]))
        col1_temp.append(float(line[5]))
        col2_temp.append(float(line[6]))
        tot_count = tot_count + 1

col1_temp = sorted(col1_temp)
col2_temp = sorted(col2_temp)
min1 = col1_temp[0]
min2 = col2_temp[0]
max1 = col1_temp[tot_count-1]
max2 = col2_temp[tot_count-1]



query_begin = 'select * from modifiedorders where '

#Generate random hyperrectangles in the space
no_queries = 2000

mlfile_name = 'dataset' + str(no_queries) + '.csv'
#queryfile_name = 'queries' + str(no_queries) + '.txt'
cardfile_name = 'card' + str(no_queries) + '.csv'

mlfile = open(mlfile_name,'w')
#queryfile = open(queryfile_name,'w')
cardfile = open(cardfile_name,'w')

curr_count = 0


while curr_count < no_queries:
    llx = round(random.uniform(min1,max1-8))
    lly = round(random.uniform(min2,max2-8))
    width = round(random.uniform(4.0,max(8.0,max1 - llx)))
    height = round(random.uniform(4.0,max(8.0,max2 - lly)))
    
    #get cardinality for this query
    card = 0
    for j in range(len(col1)):
        if col1[j] >= llx and col1[j] <= (llx + width) and col2[j] >= lly and col2[j] <= (lly + height):
            card = card + 1
    if card == 0:
        continue
    curr_count = curr_count + 1
    cardfile.write(str(card) + '\n')
    
    #File for ML program
    mlfile.write(str(llx) + ' ' + str(llx + width) + ' ' + str(lly) + ' ' +str(lly + height) + '\n')
    #create query based on the rectangle
    query = query_begin + col1_name + ' >= ' + str(llx) + ' and ' + col1_name + ' <= ' + str(llx + width) + ' ' + col2_name + ' >= ' + str(lly) + ' and ' + col2_name + ' <= ' + str(lly + height) + ';'
    #queryfile.write(query + '\n')

'''

card = 0
for j in range(len(col1)):
    if col1[j] >= 0 and col1[j] <= 12 and col2[j] >= 16 and col2[j] <= 30:
        card = card + 1

print (card)

'''

'''

col1_name = 'order_hour_of_day'
col2_name = 'days_since_prior_order'
col3_name = ''
col1 = []
col2 = []
col3 = []
col1_temp = []
col2_temp = []
col3_temp = []
tot_count = 0

with open('modifiedorders.csv') as fin:
    csv_reader = csv.reader(fin, delimiter=',')
    for line in csv_reader:
        if(len(line) < 7):
            continue
        col1.append(float(line[5]))
        col2.append(float(line[6]))
        col3.append()
        col1_temp.append(float(line[5]))
        col2_temp.append(float(line[6]))
        col3_temp.append()
        tot_count = tot_count + 1

col1_temp = sorted(col1_temp)
col2_temp = sorted(col2_temp)
col3_temp = sorted(col3_temp)
min1 = col1_temp[0]
min2 = col2_temp[0]
min3 = col3_temp[0]
max1 = col1_temp[tot_count-1]
max2 = col2_temp[tot_count-1]
max3 = col3_temp[tot_count-1]

query_begin = 'select * from modifiedorders where '

#Generate random hyperrectangles in the space
no_queries = 1000

mlfile_name = 'nextdataset' + str(no_queries) + '.csv'
queryfile_name = 'nextqueries' + str(no_queries) + '.txt'
cardfile_name = 'nextcard' + str(no_queries) + '.csv'

mlfile = open(mlfile_name,'w')
queryfile = open(queryfile_name,'w')
cardfile = open(cardfile_name,'w')

curr_count = 0

while curr_count < no_queries:
    llx = round(random.uniform(min1,max1))
    lly = round(random.uniform(min2,max2))
    llz = round(random.uniform(min3,max3))
    width = round(random.uniform(0.0,max1 - llx))
    height = round(random.uniform(0.0,max2 - lly))
    breadth = round(random.uniform(0.0,max3 - llz))
    
    #get cardinality for this query
    card = 0
    for j in range(len(col1)):
        if col1[j] >= llx and col1[j] <= (llx + width) and col2[j] >= lly and col2[j] <= (lly + height) and col3[j] >= llz and col3[j] <= (llz + breadth):
            card = card + 1
    if card == 0:
        continue
    curr_count = curr_count + 1
    cardfile.write(str(card) + '\n')
    
    #File for ML program
    mlfile.write(str(llx) + ' ' + str(llx + width) + ' ' + str(lly) + ' ' +str(lly + height) + ' ' + str(llz) + ' ' +str(llz + breadth) + '\n')
    #create query based on the rectangle
    query = query_begin + col1_name + ' >= ' + str(llx) + ' and ' + col1_name + ' <= ' + str(llx + width) + ' and ' + col2_name + ' >= ' + str(lly) + ' and ' + col2_name + ' <= ' + str(lly + height) + ' and ' + col3_name + ' >= ' + str(llz) + ' and ' + col3_name + ' <= ' + str(llz + breadth) + ';'
    queryfile.write(query + '\n')

'''
