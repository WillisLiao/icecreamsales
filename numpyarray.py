import numpy as np
n1, m1, n2, m2 = map(int, input().split())
a=np.array(list(map(int, input.split())))
b=np.array(list(map(int, input.split())))
print(a.reshape(n1,m1))
print(b.reshape(n2,m2))
c= np.zeros([n1,m2], dtype=int)