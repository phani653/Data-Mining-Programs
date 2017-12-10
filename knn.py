
import math
import csv
import random
import operator
with open(r'IRIS.csv')as csvfile:
    data=list(csv.DictReader(csvfile))
   
    #print(len(data))
    trainset=[]
    testset=[]
    split=0.67
    data.remove(data[0])
#    print(data)
    for x in range(len(data)):
    
     if random.random() <split:
            trainset.append(data[x])
     else:
            testset.append(data[x])
            
#print(len(trainset))

print(len(testset))  
def power(x):
    return math.pow(x,2)
k=5
distDict={}
storeFirstK=[]
#print(testset)
outPutClass=[]
for x in range(len(testset)):
    testRow=testset[x]
    x1= float(testRow['sepal_length']); x2= float(testRow['sepal_width']); x3=float(testRow['petal_length']);x4=float(testRow['petal_width'])
   
    for y in range(len(trainset)):
        trainRow=trainset[y]
        y1= float(trainRow['sepal_length']); y2= float(trainRow['sepal_width']); y3=float(trainRow['petal_length']);y4=float(trainRow['petal_width'])
        dis=0
        dis= math.sqrt( power(x1-y1) + power(x2-y2) + power(x3-y3) + power(x4-y4) ) 
        
        distDict[y]= dis #adding distance and row number to dictionary as key and value pair

    sorted_dict = sorted(distDict.items(), key=operator.itemgetter(1))
    #print(sorted_dict)
    nearest= sorted_dict[0][0]
    if trainset[nearest]['species']== 'setosa':
        outPutClass.append('setosa')
    elif trainset[nearest]['species']== 'versicolor':
        outPutClass.append('versicolor')
    else:
        outPutClass.append('virginica')
#    for i in range (0,k):
#        storeFirstK.append(sorted_dict[i][0])
#    c1=0; c2=0; c3=0;
#    #print(storeFirstK)
#    for i in range(0,k):
#        z=storeFirstK[i]
#        if trainset[z]['species']== 'setosa':
#            c1=c1+1;
#        elif trainset[z]['species']== 'versicolor':
#            c2=c2+1
#        else:
#            c3=c3+1
#    mx= max(c1,c2,c3)
#    if mx==c1:
#        outPutClass.append('setosa')
#        #testset[x]['species']='setosa'
#    elif mx==c2:
#        outPutClass.append('versicolor')
#        #testset[x]['species']='versicolor'
#    else:
#        outPutClass.append('virginica')
#        #testset[x]['species']='virginica'   
#    
    del storeFirstK[:]
    distDict.clear()
    del sorted_dict[:]
   

changedClas=0
for i in range (len(testset)):
    row=testset[i]
    if row['species']!= outPutClass[i]:
        changedClas=changedClas+1
        
#print (len(testset))
#print (changedClas)
print(outPutClass)
print(len(outPutClass))