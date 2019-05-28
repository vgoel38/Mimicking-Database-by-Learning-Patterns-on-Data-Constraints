import csv
import sys
import copy
import random

def warn(*args, **kwargs):
    pass

datasetfile = open('jobdataset.txt','w')
cardfile = open('jobcard.txt','w')



with open('aka_title.txt') as fin:
    for line in fin:
        dict = {'a.id':'448814','a.kind_id':'7', 'a.movie_id':'3398411','a.production_year':'2022'}
        line1 = line.split(' ')
        i = 1
        if(line1[len(line1)-2] == '0'):
            print (line1)
            continue
        while(i < len(line1)-2):
            dict[line1[i]] = line1[i+2]
            i = i + 3
        cardfile.write(line1[len(line1)-2] + '\n')
        datasetfile.write('1 ' + dict['a.id'] + ' 1 ' + dict['a.kind_id'] + ' 0 ' + dict['a.movie_id'] + ' 1875 ' + dict['a.production_year'] + '\n')
