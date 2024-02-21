from Packages.inputs import check
import math
def add(*numbers):
    """
    Adds together all parameters if they are valid.

    Returns:
        float: The sum of the parameters. None if any of the parameters aren't floats/integers.
    """
    result = 0
    
    for number in numbers:
        valid = check.is_decimal(number)
        if valid == True:
            result += 1
    
    if result == 0:
        return sum(numbers)
    return None

def multiply(*numbers):
    """
    Multiplies all parameters together if they are valid.

    Returns:
        float: The result of the calculation. None if any of the parameters aren't floats/integers.
    """
    result = 0
    
    for number in numbers:
        valid = check.is_decimal(number)
        if valid == True:
            result += 1
    
    if result == 0:
        return math.prod(numbers)
    return None

def factorial(number):
    """
    Calculates the factorial of the integer supplied.

    Args:
        number (integer): The number to find the factorial of.

    Returns:
        integer: The factorial of parapeter number. None if the parameter isn't an integers.
    """
    valid = check.is_integer(str(number))
    if valid == True:
        return factorialFunc(int(number))
    return None

def factorialFunc(number):
    """
    The backbone for the factorial function. For parameter checking please use .factorial instead of .factorialFunc.

    Args:
        number (integer): The number to find the factorial of.

    Returns:
        integer: The factorial of parapeter number.
    """
    if number == 1:
        return number
    return number * factorialFunc(number-1)