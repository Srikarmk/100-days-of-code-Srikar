import numpy as np

a=np.array([[1,2,3],[2,3,4],[6,7,8]])

# for row in a:
#     for i in row:
#         print(i)


for i in a.flat:
    print(i)