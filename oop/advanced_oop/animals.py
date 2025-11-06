from abc import ABCMeta, abstractmethod # import classes and functions from abstract base class(abc)




class Animal:
    def walk(self):
        return"walking..."
    # def num_legs(self):
    #     return 4
    @abstractmethod
    def num_legs(self):
        pass


class Dog(Animal):
    def __init__(self,name):
        self.name = name
    def num_legs(self):
        return 4

class Monkey(Animal):
    def __init__(self,name):
        self.name = name
    def num_legs(self):
        return 2

dog = Dog("buchila")
print("number of legs",dog.num_legs())
monkey = Monkey("chilada")
print(f"info about monkey:\n lengs: {monkey.num_legs()}, {monkey.walk()}")