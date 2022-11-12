import numpy as np 
import sys 
import time 

l=range(10000000)
print(sys.getsizeof(5)*len(l))

a= np.arange(1000000)
print(a.size*a.itemsize)