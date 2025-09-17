friends = ["Rolf","Bob","Jen","Anne","Semira","Teklye"]
time_since_seen = [3,7,15,11,21]
'''
zip built in function used to map first list value to second lists value corresponding to their index so as to make dictionary until shortest lenght elements reached
'''
friends_seen_time = dict(zip(friends,time_since_seen))
print(friends_seen_time)

"""
enumerate function: return index and value at that index

"""
for index, value in enumerate(friends):
    print(index, value)
# or 
print(list(enumerate(friends)))
"""
lambda function: it is anonemous function

"""
x = 20
y = 5
divide = lambda x,y: x/y  
print(divide(x,y))
print((lambda x,y: x/y)(10,20))

students = [
    {"name": "Rolf", "grades":(67,90,95,100)},
    {"name": "Bob", "grades":(56,78,80,90)},
    {"name": "Jen", "grades":(98,90,95,100)},
    {"name": "Anne", "grades":(100,100,95,100)}
]
def average(grades):
    return sum(grades)/len(grades)
for student in students:
    print((lambda grades: sum(grades)/len(grades))(student["grades"]))



class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades
    

    def average(self):
        return sum(self.grades)/len(self.grades)
student_one = Student("bob",[21,13])
print("\n"*10)
ave = student_one.average()
print(ave)
ave = Student.average(student_one)
'''
when we use object.method() python perform object_class.method(object) underneath the hood
'''
print(ave)
print(student_one.__class__)

class Movie:
    def __init__(self, name,year):
        self.name = name
        self.year = year
print(Movie("The Matrix",1994).name)

class Garage:
    def __init__(self):
        self.cars = []
    def __len__(self):
        return len(self.cars)
    def __getitem__(self, index):
        return self.cars[index]
    def __repr__(self):
        return f'<Garage {self.cars}'
    def __str__(self):
        return f'Garage with {len(self)} cars'


    def addCars(self,car):
        self.cars.append(car)
ford = Garage()
ford.addCars("Fiesta")
ford.addCars("Focus")
print(len(ford.cars),len(ford),len(ford.cars)==len(ford))
print(ford[0]) # == print(Garage.__getitem__(ford,0))
print(Garage.__getitem__(ford,0))
print("\n"*5)
for car in ford: # len and getitem dinder method must created in objects class to use the object as iterable
    print(car)
print(ford)

if __name__ == "__main__":
    print("We are on the mail module")