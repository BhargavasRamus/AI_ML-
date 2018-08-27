import numpy as np
import pandas

def euclidean_dist(X_test,X):
	dist = np.zeros((1000,1))
	for j in range(0,1000,1):
		dist[j] = np.sqrt((X_test[0]-X[j][0])**2)+((X_test[1]-X[j][1])**2)
	dist = np.reshape(dist,1000)
	return dist

def bubbleSort(array):
    for passnum in range(len(array)-1,0,-1):
        for i in range(passnum):
            if alist[i]>array[i+1]:
                temp = array[i][0]
                array[i] = array[i+1]
                array[i+1] = temp
                temp1 = array[i][1]
                array[i][1] = array[i+1][1]
                array[i+1][1] = temp1
    return array

X_0=pandas.read_csv("X.csv")
Y_0=pandas.read_csv("Y.csv")
X=np.transpose(np.array(X_0, dtype=np.float64))
Y=np.array(Y_0, dtype=np.float64)

X_test = np.array([[1,1],[1,-1],[-1,1],[-1,-1]])

print("enter the value of K \n")
K = input()
K = int(K)

for i in range(0,len(X_test)):
	dist = euclidean_dist(X_test[i],X)
	dist_Y = np.transpose(np.array((dist,Y.reshape(1,1000))))
	sort_1 = bubbleSort(dist_Y)
	K_elems = sort_1[:K]
  K_elems = K_elems.ravel()
	expectation = np.sum(K_elems[-k:])
	if expectation>0 :
		print(X[i],"corresponds to Y=1 \n")
	else:
		print(X[i],"corresponds to Y=-1 \n")
