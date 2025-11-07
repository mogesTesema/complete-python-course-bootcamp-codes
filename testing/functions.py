from typing import Union

def divide(dividend:Union[int,float],divisor:Union[int,float]):
    if divisor == 0:
        raise ValueError("Divisor can't be Zero")
    return dividend/divisor

# print("division results:\n",divide(10,2.3))

def multiply(*args:Union[int,float]):
    if len(args) == 0:
        raise ValueError("At least one value is mandatory")
    total = 1
    for arg in args:
        total *= arg
    return total

