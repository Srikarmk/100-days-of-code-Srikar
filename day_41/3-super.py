class Animal():
    is_alive=True
    def __init__(self,fur,wings):
        self.has_fur=fur
        self.has_wings=wings
    def eats(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Tiger(Animal):
    def __init__(self, fur, wings):
        super().__init__(fur, wings)
        if fur==True:
            print("Tiger has fur")
        if wings==True:
            print("Tiger has wings")
    def hunts(self,hunts):
        self.hunts=hunts
        if self.hunts==True:
            print("Tiger is a predator")
        else:
            print("TIger doesn't hunt")
    
tiger=Tiger(True,False)


