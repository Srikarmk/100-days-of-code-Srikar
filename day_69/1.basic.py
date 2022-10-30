import  numpy as np

# # a=np.array([[1,2],[2,3],[3,4]])
# # print(type(a)) 
# # print(a.ndim)
# # print(a.itemsize)
# # print(a.dtype)
# # print(a.size)
# # print(a.shape)

# # o=np.ones((3,4))
# # print(o)

# # a=np.arange(500)
# # print(a)

# # a=np.linspace(1,10,20)
# # print(a)

a=np.array([
    [1,2],
    [2,3],
    [3,4]
])
print(a)
print(a.shape)
# print(a.reshape(2,3))
# # a=a.ravel()
# # print(a)
# print(a.min())
# print(a.max())
# print(a.sum(axis=0))
# print(np.sqrt(a))

# print(np.std(a))
# #adding 2 list items
# # l1=[1,2,3]
# # l2=[1,2,3]
# # print([(x+y) for x,y in zip(l1,l2)])