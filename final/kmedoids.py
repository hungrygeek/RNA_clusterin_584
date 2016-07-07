import numpy as np
import random

#assign seqs to clusters based on distance matrix
def assignClusters(medoids, dMatrix):
    disMedoids = dMatrix[:,medoids]
    clusters = medoids[np.argmin(disMedoids, axis=1)]
    clusters[medoids] = medoids
    return clusters

#update the medoid based on the current cluster results
def updateMedoids(kMedoidsCluster, dMatrix):
    mask = np.ones(dMatrix.shape)
    mask[np.ix_(kMedoidsCluster,kMedoidsCluster)] = 0.
    clusterDis = np.ma.masked_array(data=dMatrix, mask=mask, fill_value=10e9)
    costs = clusterDis.sum(axis=1)
    return costs.argmin(axis=0, fill_value=10e9)
   
#main method   
def kMedoidsCluster(dMatrix, k,maxIter):
    numPoints = dMatrix.shape[0] 
    # Initialize k random medoids.
    currMedoids = np.array([-1]*k)
    
    while not len(np.unique(currMedoids)) == k:
        currMedoids = np.array([random.randint(0, numPoints - 1) for _ in range(k)])
    preMedoids = np.array([-1]*k)
    newMedoids = np.array([-1]*k)
   
    # while loop for medoids to updates
    counter=1
    while not ((preMedoids == currMedoids).all() or counter>maxIter):
        # Assign each point to kMedoidsCluster with closest medoid.
        clusters = assignClusters(currMedoids, dMatrix)

        # Update medoids
        for medoid in currMedoids:
            kMedoidsCluster = np.where(clusters == medoid)[0]
            newMedoids[currMedoids == medoid] = updateMedoids(kMedoidsCluster, dMatrix)

        preMedoids[:] = currMedoids[:]
        currMedoids[:] = newMedoids[:]
        counter=counter+1

    return clusters   
   
   
   
   
   