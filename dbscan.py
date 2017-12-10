# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 15:07:55 2017

@author: Student
"""

import csv
from random import randint
with open ('iris.csv','r') as f:
    reader= csv.DictReader(f)
    dataset= list(reader)

f = open('dbOut.txt', 'w')
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

arbitaryPoints=[]
visited=[]
for i in range(0,n):
    visited.append(0)
    arbitaryPoints.append(i)

eps=2
minpoints=20

allClusters=[]
noisePoints=[]
while (1):
    arbLen= len(arbitaryPoints)
    if arbLen <= minpoints:
        for i in range(0,n):
            if visited[i]==0:
                noisePoints.append(i)
        break
        
    rdInt= randint(0,arbLen-1)
    arbitary= arbitaryPoints[rdInt] #choosing a random point in range
    if visited[arbitary] !=1: # if this not included in any cluster
        thisTotal = totals[arbitary] #take what is its total
        thisCluster=[] #ready to form a new cluster
        
        for i in range(0,n):
            if visited[i]==0: #if not included in any cluster
                varA= abs(thisTotal-totals[i]) # measuring how much distance
                if varA <= eps: #if distance less than epsilon
                    thisCluster.append(i)
                    visited[i]=2 # this is for future purpose. If this cluster not satisfied to exclude it
    
        if len(thisCluster) < minpoints:
            for i in range(0,n):
                if visited[i]==2:
                    visited[i]=0
        else:
            for i in range(0,n):
                if visited[i]==2:
                    visited[i]=1
                    arbitaryPoints.remove(i)
    
        allClusters.append(thisCluster)
        f.write("\n Cluster \n")
        for i in range(0,len(thisCluster)):
            f.write(str(thisCluster[i]))
            f.write(" ")
        f.write("\n\n")
        del thisCluster
    
    if sum(visited) >=n:
        break
f.write("\n\nNoise points\n\n")
for i in range(0,len(noisePoints)):
    f.write(str(noisePoints[i]))
    f.write(" ")
    
f.close();