# t=open("P:\Python\Learning\\basic.txt")
# text=t.readlines()
# print(text)
# t.close()


count=0
if count==0:
    with open ("P:\Python\Learning\\basic.txt","a") as fl:
        fl.write("Hello")
        count+=1




with open ("P:\Python\Learning\\basic.txt") as fl:
    tx=fl.read()
    print(tx)