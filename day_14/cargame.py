cmd=input(">")
if cmd=="help":
    print("Start - Start Car ")
    print("Stop - Stop Car ")
    print("Quit - exit")

print(" ")
while(cmd=="help"):
    car=input(">")
    if car=="Start":
        print("Your car is Starting......")   
    elif car=="Stop":
        print("Your car is Stopping......")   
    elif car=="Quit":
        print("Exit")
        break
    else:
        print("Unrecognized cmd")
else:
    print("Unrecognized cmd")

