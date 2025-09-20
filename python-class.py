"""
create chatbot class with the following attribute and method:
1. __init__ 
2. __len__
3. __getint__
4. __repr__
5. __str__
6. chat()
7. history()
    can view n most recent chats, and delete any chat if necessary
8. recent()
"""

import heapq
from datetime import datetime
class ChatBot:
    def __init__(self,name):
        self.name = name
        self.chats = []

    def __len__(self):
        return len(self.chats)

    def __getitem__(self,index):
        return self.chats[index][1]

    def __repr__(self):
        return f"chatbot with {self.chats} chats"

    def __str__(self):
        return f"chatbot system that interact with user that has {len(self.chats)} chats till now."

    def chat(self,chat):
        curr = datetime.utcnow()
        self.chats.append((curr,chat))

    def history(self):
        return [chat[1] for chat in self.chats]

    def recent(self,n=0):
        heapq.heapify(self.chats)
        if n == 0:
            return [self.chats[0][1]]
        most_recent = heapq.nsmallest(n,self.chats)
        return [chat[1] for chat in most_recent]
    def oldest(self,n = 1):
        most_oldest = heapq.nlargest(n,self.chats)
        return [chat[1] for chat in most_oldest ]

    def delete(self,index):
        return self.chats.pop(index)[1]
user = ChatBot("user")
print(user)
user.chat("what is Machine Learning?")
user.chat("what is AI?")
user.chat("what is Deep Learning?")
user.chat("why we care about tech?")
history = user.history()
print(history)
print(user)
print(user.recent(3))
print(user.delete(0))
print(user.history())
print(user.recent(2))
user.chat("I think machine learning is the future Engineer")
user.chat("I think you will fail in bad condition unless you focus on what matter for you right now")
user.chat("to be AI engineer or ML engineer, fullstack software development is the first journey you should go.")
print(user.history())
print(user.recent(),user.oldest())
print("\n"*4)
for chat in user:
    print(chat)
print(len(user))
"""
inheritance is the beauty of OOP what encourage DRY principle(Don't repeat yourself)
"""
class ProfChatBot(ChatBot):
    def __init__(self,name,title,salary=0):
        super().__init__(name)
        self.title = title
        self.salary = salary
    @property
    def annual_salary(self):
        return f"Hello {self.title} {self.name} your anuall salary is {self.salary*12}$."
    

prof = ProfChatBot("Alemayehu","Dr.",120)
print(prof.annual_salary)
prof.chat("why my salary is not increasing?")
prof.chat(f"Hello! I am Dr. Alemayehu. please increase my salary, I can't servive life with this {prof.salary}$ salary.")
prof.chat("if you don't increase salary, I will leave your company.")
print(prof.history())
print("\n",prof.recent())
print("\n",prof.annual_salary)

"""
Decoratory in python:
@property:- used to change simple class method to just property of the class if this method don'e perform action rather than calculation 
@classmethod:- used to pass class as argument for class method that used to get info about the class itself
@staticmethod:- used to conviy info about the class but don't use neither class properties nor class method
#instancemethod:- used to pass instance(object) of the class to access propertiy and method of the instance for its usecase(every method in class is by default such type of method )
"""

class Foo:
    @classmethod # this decorator used to pass class as argument 
    def hi(cls): # take the objects class as argument
        return print(cls.__name__) 
    @staticmethod
    def hello():
        print("ell, I don't take parameters.")

foo_object = Foo()
foo_object.hi()
foo_object.hello()
class FixedFloat:
    def __init__(self,amount):
        self.amount = amount
    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}"
    @classmethod
    def from_sum(cls,value_one, value_two):
        return cls(value_one + value_two)

number = FixedFloat(18.5762)
print(number)
new_number = FixedFloat.from_sum(10.244,242.2424)
print(new_number)
  
class Dollar(FixedFloat):
    def __init__(self,amount):
        super().__init__(amount)
        self.symbol ='$'
    def __repr__(self):
        return f"<Dollar {self.symbol}{self.amount:.2f}"
money = Dollar(18.2424)
print(money)
dollar = Dollar.from_sum(4243.3434,34.3434)
print(dollar)
print(dir(heapq))
print(datetime.now())
import json
print(dir(json))
x = {
  1: "John",
  2: 30,
  3: "New York"
}
y = json.dumps(x)
print(y)
x = json.loads(y)
print(x)
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
import re
print(dir(re))