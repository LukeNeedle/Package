def add(*numbers):
    valid = True
    for number in numbers:
        if valid == False:
            number, valid = inputs.check.integer(number)
    return sum(numbers)