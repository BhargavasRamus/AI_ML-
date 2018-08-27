import numpy as np
import pandas

X_0=pandas.read_csv("X.csv")
Y_0=pandas.read_csv("Y.csv")
X=np.transpose(np.matrix(X_0).astype(float))
Y=np.matrix(Y_0).astype(float)
X_test = np.array([[1,1],[1,-1],[-1,1],[-1,-1]])

N=0
M=0
for i in range(0,len(Y)):
    if Y[i]==-1.0:
        
        X_1=X_1.drop(X_1.index[i-N])
        N=N+1
    if Y[i]==1.0:
        
        X_2=X_2.drop(X_2.index[i-M])
        M=M+1
V_X1=np.var(X_1)
V_X2=np.var(X_2)
M_X1=np.mean(X_1)
M_X2=np.mean(X_2)

for i in range(0,len(X_test)):
    pr_1 = (len(X_1)/(len(Y)*np.sqrt(2*np.pi*V_X1[0,1]*V_X1[0,0])))*np.exp(-((X_test[i][0]-M_X1[0,0])**2)/(2*V_X1[0,0]))*np.exp(-((X_test[i][1]-M_X1[0,1])**2)/(2*V_X1[0,1]))
    pr_2 = (len(X_2)/(len(Y)*np.sqrt(2*np.pi*V_X2[0,1]*V_X2[0,0])))*np.exp(-((X_test[i][0]-M_X2[0,0])**2)/(2*V_X2[0,0]))*np.exp(-((X_test[i][1]-M_X2[0,1])**2)/(2*V_X2[0,1]))

if pr_1>pr_2:
  print("the test sample corresponds to Y=1")
else:
  print("the test sample corresponds to Y=-1")
