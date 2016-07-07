import scipy.cluster.hierarchy as hac
import numpy as np
import csv
from matplotlib import pyplot as plt

import maxOverlap as mo
import kmedoids as km
#transfer distance matrix into condense form
def matrixTrans(dMatrix):
	n=len(dMatrix)
	disVec=np.zeros(n*(n-1)/2)
	#disVec=[]
	counter=0
	condensed_idx = lambda i,j,n: i*n + j - i*(i+1)/2 - i - 1
	for i in range(n):
		for j in range(i+1,n):
			#disVec[0,counter]=dMatrix[i,j]
			disVec[condensed_idx(i, j, n)]=dMatrix[i,j]
			#disVec.append(dMatrix[i,j])
			counter=counter+1
	return disVec

#compute linkage, dendogram and outperm order		
def outPerm(dMatrix):
	disVec=matrixTrans(dMatrix)
	tree=hac.linkage(disVec,'average')
	R=hac.dendrogram(tree)
	plt.show()
	plt.close()
	return R

#take outperm and generate heatmap
def heatmap(dMatrix):
	outpermDic=outPerm(dMatrix)
	outperm=outpermDic['leaves']
	labels=outpermDic['ivl']
	temp=dMatrix[outperm,:]
	sortedDM=temp[:,outperm]
	n=len(sortedDM)
	list_x=[]
	for i in range(n):
		list_x.append(i+1)
	x, y = np.meshgrid(list_x, list_x)
	#now plug the data into pcolormesh
	plt.pcolormesh(x, y, sortedDM,vmin=0,vmax=1)
	#plt.xlim(1,n)
	#plt.ylim(1,n)
	plt.colorbar()
	plt.show()
	ff=open('hrTestTable.csv','w')
	for i in range(12):
	
		curList=outperm[41*i:41*(i+1)]
		ff.write(str(i))
		ff.write(',')
		#compute mean and vairance
		ff.write(str(np.mean(curList)))
		ff.write(',')
		ff.write(str(np.std(curList)))
		ff.write('\n')
	
f= csv.reader(open("testSeq.csv","rb"))

