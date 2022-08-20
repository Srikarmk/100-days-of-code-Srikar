t=int(input())
sum1,sum2=0,0
for i in range(1,t+1):
    a,b=map(int,input().split())
    if (a+i)%i==0 and (b+2*i)%(i)==0:
        print("Yes")
    else:
        print("No")
   
    '''for _ in range(0,100000):
        sum1+=(a+i)
        sum2+=(b+(i*2))
        if sum1==sum2:
            print("Yes")

    else:
        print("No")
       # _+=1'''
        
      
