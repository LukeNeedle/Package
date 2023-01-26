from Packages.inputs import check
import math
def add(*numbers):
    valid = True
    for number in numbers:
        if valid == False:
            number, valid = check.decimal(number)
    return sum(numbers)

def multiply(*numbers):
    valid = True
    for number in numbers:
        if valid == False:
            number, valid = check.decimal(number)
    return math.prod(numbers)

def factorial(number):
    number, valid = check.integer(number)
    if valid:
        return factorialFunc(number)

def factorialFunc(number):
    if number == 1:
        return number
    return number * factorialFunc(number-1)