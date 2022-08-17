import numpy as np

read_input = lambda tp: list(map(tp, input().split()))
num_features, n = read_input(int)
X = []
for i in range(n):
    X.append(read_input(float))
    
X = np.array(X, dtype=np.float64)
Y = X[:, -1]
X = X[:, :-1]

t = read_input(int)[0]
Xtest = []
for i in range(t):
    Xtest.append(read_input(float))
Xtest = np.array(Xtest, dtype=np.float64)

def solve():
    xinterval = n // 5
    Xnew = []
    Ynew = []
    for i in range(4):
        Xnew.append([np.mean(X[i*xinterval: (i+1)*xinterval]**j, axis=0) for j in range(4, -1, -1)])
        Ynew.append(np.mean(Y[i*xinterval: (i+1)*xinterval]))
    Xnew.append([np.mean(X[4*xinterval:]**j, axis=0) for j in range(4, -1, -1)])
    Xnew=  np.array(Xnew)
    Ynew = np.array(Ynew)
    print(Xnew.shape)
    print(np.linalg.tensorinv(Xnew, ind=0).shape)
    
    

solve()
