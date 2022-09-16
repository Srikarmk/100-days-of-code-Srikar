class Solid():
    def structure(self):
        print("This has a rigid structure")
    def shape(self):
        print("Can be any 3D Shape")
class Liquid():
    def structure(self):
        print("This has a fluid structure")
    
class Oil(Liquid):
    pass
class Water(Liquid,Solid):
    pass 

water=Water()
water.structure()
water.shape()