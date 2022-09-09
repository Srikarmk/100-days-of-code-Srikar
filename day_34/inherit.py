class car:
    def fuel(self,fuel):
        self.fuel=fuel
        print("This is a "+fuel+" car") 
    def gears(self):
        pass 
    def wheel_type(self):
        pass
class Altroz(car):
    def fuel(self):
        pass
    def gears(self):
        return super().gears()
    def wheel_type(self):
        return super().wheel_type()

base=car()
base.fuel("Petrol")
tata=Altroz()
print(tata.fuel())