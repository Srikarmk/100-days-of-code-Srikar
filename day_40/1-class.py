class Car():
    wheels=4  #class variables
    def __init__(self,model):  #constructor with attribute
        self.model=model #instance variables 
    def fuel(self,fuel): #method
        self.fuel=fuel
        print(self.model+" uses "+self.fuel)
    def color(self,color):
        self.color=color
        print(self.model+" is "+self.color)

lambo=Car('Lamborghini')

lambo.color('Orange')
lambo.fuel('Diesel')
print(lambo.wheels)