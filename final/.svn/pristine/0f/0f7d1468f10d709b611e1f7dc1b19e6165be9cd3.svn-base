import numpy as np
import csv

import maxOverlap as mo
import kmedoids as km
from collections import defaultdict


f= csv.reader(open("testSeq.csv","rb"))

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
#operate k-mmedoids
clusterLabel=km.kMedoidsCluster(distM, numClus,maxIter)
dicResult = defaultdict(list)
a=[]
counter=0
print clusterLabel
for i in clusterLabel:	
		dicResult[i].append(float(positionM[counter]))
		counter=counter+1

ff=open('kmTestTable.csv','w')
for key in dicResult.iterkeys():
	
	curList=dicResult[key]
	print curList
	ff.write(str(key))
	ff.write(',')
	#compute mean and vairance
	ff.write(str(np.mean(curList)))
	ff.write(',')
	ff.write(str(np.std(curList)))
	ff.write('\n')
