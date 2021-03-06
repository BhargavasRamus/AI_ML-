import numpy as np
import pandas

X_0=pandas.read_csv("X.csv")
Y_0=pandas.read_csv("Y.csv")
X=np.transpose(np.array(X_0, dtype=np.float64))
Y=np.array(Y_0, dtype=np.float64)
X_test = np.array([[1,1],[1,-1],[-1,1],[-1,-1]])

X_1=X
X_2=X
N=0
M=0
for i in range(0,len(Y)):
    if Y[i]==-1.0:
        
        X_1=np.delete(X_1,i-N,axis=0)
        N=N+1
    if Y[i]==1.0:
        
        X_2=np.delete(X_2,i-N,axis=0)
        M=M+1
V_X1=np.var(X_1,axis=0)
V_X2=np.var(X_2,axis=0)
M_X1=np.mean(X_1,axis=0)
M_X2=np.mean(X_2,axis=0)

for i in range(0,len(X_test)):
    pr_1 = (len(X_1)/(len(Y)*np.sqrt(2*np.pi*V_X1[0,1]*V_X1[0,0])))*np.exp(-((X_test[i][0]-M_X1[0,0])**2)/(2*V_X1[0,0]))*np.exp(-((X_test[i][1]-M_X1[0,1])**2)/(2*V_X1[0,1]))
    pr_2 = (len(X_2)/(len(Y)*np.sqrt(2*np.pi*V_X2[0,1]*V_X2[0,0])))*np.exp(-((X_test[i][0]-M_X2[0,0])**2)/(2*V_X2[0,0]))*np.exp(-((X_test[i][1]-M_X2[0,1])**2)/(2*V_X2[0,1]))
    if pr_1>pr_2:
        print(X_test[i],"corresponds to Y=1")
    else:
        print(X_test[i],"corresponds to Y=-1")
