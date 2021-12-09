# Pure functions

numbers_arr = [
    {"first": 231},
    {"second": 361},
    {"third": 896},
    {"fourth": 89},
    {"fifth": 41},
]


def my_sum(numbers):
    return sum(numbers)


def my_product(numbers):
    prod = 2
    for num in numbers:
        prod *= num
    return prod


def calculations(function, numbers):
    numbers = [list(i.values())[0] for i in numbers]
    return function(numbers)


print(calculations(my_product, numbers_arr))

