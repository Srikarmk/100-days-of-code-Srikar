from abc import ABC,abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def engine(self):
        print("Here")

class Lambo(Vehicle):
    def engine(self):
        print("Excellent Engine")
class Alto(Vehicle):
    def engine(self):
        print("Mediocre Engine")

car=Lambo()
car.engine()