for i in range(0,200):
    num=i*i*i
    ctr=0
    for i in range(0,3):
        check=num%10
        if(check!=8):
            continue
        elif check==8:
            ctr+=1

if ctr==3:
    print(num)
