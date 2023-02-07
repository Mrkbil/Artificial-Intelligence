import csv
import numpy as np
import matplotlib.pyplot as plt

file=open('data.csv')
CSVdata=csv.reader(file)
datalist=[]
for row in CSVdata:
    datalist.append(row)

data=np.asarray(datalist,dtype=float)
m=data.shape[0]
n=data.shape[1]
k=6
iteration=100
centroids= np.random.randn(k,n)

plt.scatter(data[:,0],data[:,1])
plt.scatter(centroids[:,0],centroids[:,1],marker='s')
plt.show()
# print("Randomly Initialized Centroids:",centroids)
for iter in range(iteration):
    attached_centroids=[]
    for i in range(k):
        attached_centroids.append([])
    for i in range(m):
        centers = []
        for j in range(k):
            euc=0
            for f in range(n):
                euc+=(centroids[j,f]-data[i,f])**2
            euc=np.sqrt(euc)
            centers.append(euc)
        closest_center=centers.index(min(centers))
        attached_centroids[closest_center].append(data[i])

    previous_loc=np.copy(centroids)
    for i in range(k):
        attached_sample=np.asarray(attached_centroids[i])
        num_sample=attached_sample.shape[0]
        new_location=np.sum(attached_sample,axis=0)/num_sample
        centroids[i]=new_location
    print("New Centroids:",centroids)
    if np.array_equal(previous_loc, centroids):
        print("Break.")
        break

plt.scatter(data[:,0],data[:,1])
plt.scatter(centroids[:,0],centroids[:,1],marker='s')
plt.show()
