# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:57:07 2017

@author: Student
"""

import csv

with open('iris.csv', 'r') as f:
  reader = csv.DictReader(f)
  dataset = list(reader)

f = open('Agl.txt', 'w')
f.truncate()

for data in dataset:
    if data['species']=='setosa':
        data['species']=1
    if data['species']=='versicolor':
        data['species']=2
    if data['species']=='virginica':
        data['species']=3

n= len(dataset)

totals=[]

for i in range(0,n):
    tmplist= dataset[i];
    x=float(tmplist['sepal_width'])+float(tmplist['sepal_length'])+float(tmplist['petal_length'])+float(tmplist['petal_width'])+float(tmplist['species'])
    totals.append(x)

row, col=n,n
dist_mtrx=[[0 for var1 in range(row)] for var2 in range(col)]

for i in range(0,n):
    for j in range(0,n):
        if j<i:
            dist_mtrx[i][j]=99
        else:
            dist_mtrx[i][j]= abs(totals[i]-totals[j])
      
for i in range(0,n):
    for j in range(0,n):
        f.write(str(dist_mtrx[i][j]))
        f.write("\t\t")
    f.write("\n")

f.close()            
