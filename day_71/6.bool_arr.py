import numpy as np

a=np.arange(9).reshape(3,3)

b=a>4
print(b)
print(a[b])
a[b]=-1
print(a)