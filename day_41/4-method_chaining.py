class Tiger():
    def eat(self):
        print("Tiger is eating")
        return self
    def hunt(self):
        print("Tiger is hunting")
        return self
    def roar(self):
        print("Tiger is roaring")
        return self
    def sleep(self):
        print("Tiger is sleeping")
        return self


tiger=Tiger()
tiger.roar().hunt().eat().sleep()