def add(*numbers):
    valid = True
    for number in numbers:
        if valid == False:
            number, valid = check.decimal(number)
    return sum(numbers)

