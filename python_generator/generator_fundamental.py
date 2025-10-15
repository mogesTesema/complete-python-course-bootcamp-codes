def hundred_numbers_one() -> list:
    nums = []
    i = 0
    while i < 100:
        nums.append(i)
        i += 1
    return nums

def hundred_number_generator():
    i = 0
    while i < 100:
        yield i
        i += 1
# g = hundred_number_generator()

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(list(g))

# my_range_obj = range(100)

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0
    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()
# my_gen = FirstHundredGenerator()
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
            

class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1,10,2,3,4,5]
        self.i = 0
    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration()
    def __iter__(self):
        return self

class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()
my_gen = FirstFiveIterator()
print(next(my_gen))
print(next(my_gen))
print(my_gen.i)
print(my_gen.i)
print(my_gen.i)
print("done")
for i in my_gen:
    print(i)

class AnotherIterable:
    def __init__(self):
        self.cars = ["Fiesta","Focus"]
    def __len__(self):
        return len(self.cars)
    def __getitem__(self,index):
        return self.cars[index]
for car in AnotherIterable():
    print(car)
    """
    Iterable is object that has either len and getitem dunder method or that has iter dunder method in its class implementation.
    """

def starts_with_r(friend):
    return True if friend[0]=="R" else False

friends = ["Rolf","Jose","Randy","Anna","Mary"]

start_with_r = filter(lambda friend: friend.startswith("R"),friends)
another_start_with_r = (f for f in friends if f.startswith("R")) # generator compehension
print(next(start_with_r))
print(next(start_with_r))
print(list(another_start_with_r))

"""
map function
"""
friends_lower = map(lambda x: x.lower(),friends)
print(next(friends_lower))
