from typing import Union

def divide(dividend:Union[int,float],divisor:Union[int,float]):
    if divisor == 0:
        raise ValueError("Divisor can't be Zero")
    return dividend/divisor

# print("division results:\n",divide(10,2.3))