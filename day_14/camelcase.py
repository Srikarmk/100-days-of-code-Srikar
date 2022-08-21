s=input()
ctr=1
for i in range(len(s)):
    if s[i].isupper==True:
        ctr+=1
print(ctr)