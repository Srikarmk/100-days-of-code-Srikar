import numpy as np

a=np.arange(30).reshape(2,15)
# b=np.arange(6,12).reshape(3,2)
# print(np.vstack((a,b)))
# print(np.hstack((a,b)))

print(np.hsplit(a,3))
a=np.arange(30).reshape(15,2)
print(np.vsplit(a,5))


