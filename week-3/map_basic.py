numbers = [1, 2, 3, 4, 5]


def square(x):
    return x * x


squared_numbers = map(square, numbers)
squared_numbers_list = list(squared_numbers)
print(squared_numbers_list)
