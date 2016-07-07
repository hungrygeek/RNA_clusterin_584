import numpy as np
import csv

import maxOverlap as mo
import kmedoids as km

f= csv.reader(open("toySample.csv","rb"))

dataM=[]
#store data
for line in f:
	dataM.append(line)
	
#compute distance matrix
length=len(dataM)
distM=np.zeros((length, length))
overlap=20
numClus=13
maxIter=10000
for i in range(length):
	print i
	for j in range(i+1,length):
		distM[i,j]=mo.maxOverlap(''.join(dataM[i]), ''.join(dataM[j]) , overlap)
		distM[j,i]=distM[i,j]
#operate k-mmedoids
clusterLabel=km.kMedoidsCluster(distM, numClus,maxIter)
ff=open('result.csv','w')
for label in clusterLabel:
	ff.write(str(label))
	ff.write(',')
ff.close()


dataM=[]
positionM=[]
#store data
for line in f:
	dataM.append(line[0])
	positionM.append(line[1])
#compute distance matrix
length=len(dataM)
distM=np.zeros((length, length))
overlap=20
numClus=12
maxIter=100000
for i in range(length):
	print i
	for j in range(i+1,length):
		distM[i,j]=mo.maxOverlap(''.join(dataM[i]), ''.join(dataM[j]) , overlap)
		distM[j,i]=distM[i,j]

heatmap(distM)