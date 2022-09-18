class cell():
    level=1
    def has_blood(self):
        print("No blood")


class tissue(cell):
    level=100
    def has_blood(self):
        print("Yes has blood")

class organ(tissue):
    level=600
    


body=organ()
print(organ.level)
body.has_blood()