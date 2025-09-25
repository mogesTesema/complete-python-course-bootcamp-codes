class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def __repr__(self):
        return f"<Car {self.make} {self.model}>"



class Garage:
    def __init__(self):
        self.cars = []
    def __len__(self):
        return len(self.cars)
    def add_car(self,car):
        if not isinstance(car,Car):
            raise ValueError(f"Tried to add a {car.__class__.__name__} to the garage, but you can only add '{Car.__name__}' object.")
        self.cars.append(car)
        # raise NotImplementedError("We can't add cars to the garage yet")
ford = Garage()
car = Car("ford","Fiesta")
ford.add_car(car)
print(len(ford))
try:
    ford.add_car("hello")
except TypeError as e:
    print("some thing went wrong: ",e)
except ValueError as e:
    print("value error hitted:",e)
finally:
    print(f"The garage now has {len(ford)}")

class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def __repr__(self):
        return f"<Car {self.make} {self.model}>"
car = Car("make","tesla")
print(car)

class Garage:
    def __init__(self):
        self.cars = []
    def __len__(self):
        return len(self.cars)
    def __repr__(self):
        return f"<this is {Garage.__name__} class>"
    def __str__(self):
        return f"this is a garage class that used to store cars Created by \"Car\" class"
    def add_car(self,car):
        if  not isinstance(car,Car):
            raise ValueError(f"{car.__class__.__name__} is not object of {Car.__name__}")
        self.cars.append(car)

garage_a = Garage()
print(garage_a)
garage_a.add_car(car)
print(len(garage_a))
garage_b = Garage()
garage_b.add_car("ello")
