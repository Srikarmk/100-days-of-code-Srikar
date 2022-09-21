fileName=input("Enter the file name\t")
content=input("Enter the content\t")

with open(f'{fileName}','w') as fle:
    fle.write(content)

readIt=input("Do you want to read the file? [y/n]\t")

if readIt in ['y','n']:
    if readIt=='y':
        with open(fileName,'r') as fle:
            print(fle.read())
    else:
        print("Exit....")