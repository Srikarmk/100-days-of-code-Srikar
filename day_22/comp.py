# l=[[x,x**2,x**3] for x in range(10)]
# print(l)

# l=[x if x%2==0 else x+100 for x in range(200) ]
# print(l)

l=[a+b for a in [1,2,3] for b in [3,4,5]]
n=[[a+b for a in [1,2,3]]for b in[3,4,5]]
print(l,n)