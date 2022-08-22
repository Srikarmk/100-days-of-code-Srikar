from dis import dis
import math
#clculate euclidian distance between (p1,q1) and (p2,q2)
p1,p2,q1,q2=3,4,6,5
dist=math.sqrt(math.pow(q1-p1,2)+math.pow(q2-p2,2)) 
print(dist)