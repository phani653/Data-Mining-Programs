# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:04:48 2017

@author: programmer
"""

import csv

with open('kmData.csv','r') as f:
    lis=[line.split() for line in f]
    reader= csv.DictReader(f)
    dataset= list(reader)


mrk1=[]; mrk2=[]; mrk3=[]; mrk4=[]
for data in dataset:
    mrk1.append(data['m1']) #column m1 can be read by this into mrk1
    mrk2.append(data['m2'])
    mrk3.append(data['m3'])
    mrk4.append(data['m4'])

totals=[]
for i in range(1,2):
    tmp_list= lis[i]
    
    
