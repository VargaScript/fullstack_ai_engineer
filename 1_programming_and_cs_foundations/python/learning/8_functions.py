#Exercises

number_1 = 3
number_2 = -7
number_3 = 12

name_1 = "Adair"
name_2 = "Lucía"
name_3 = "Carlos"

num_list = [-10, 0, 4, 99, -3]

factorial_inputs = [0, 1, 3, 5, 7]

fibonacci_limits = [5, 10, 20]

grades_1 = [90, 80, 70, 100]
grades_2 = [56, 76, 89, 92, 78, 88]
grades_3 = [10, 20]

nested_list_1 = [1, [2, [3, 4], 5]]
nested_list_2 = [[1, 2], [3, 4], 5]
nested_list_3 = [1, [2, [3, [4, [5]]]]]

def square(x):
    return x * x

def to_upper(text):
    return text.upper()

numbers = [1, 2, 3, 4, 5]
names = ["adair", "lucía", "carlos"]

#1 Write a function that returns the square of a number.
def square_number(number):
    return number ** number

print(square(number_3))

#2 Create a function that greets a user by name.
def greeting(username):
    return f"Hello, good morning {username}!"

print(greeting(name_3))

#3 Write a function that checks if a number is positive.
def check_if_positive(list_of_numbers):
    for number in list_of_numbers:
        if number >= 0:
            print(f"The number {number} is positive")
        else: 
            print(f"The number {number} is negative")

check_if_positive(num_list)

#4 Create a function that returns the factorial of a number.
def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)
    
for number in factorial_inputs:
    print(f"The factorial of {number} is {factorial(number)}")
    
#5 Write a function that returns the Fibonacci sequence up to n.
def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

for number in fibonacci_limits:
    print(f"The fibonacci number of {number} is {fibonacci(number)}")

#6 Write a function that accepts a list and returns the average.
def return_average(list):
    sum = 0
    for number in list: 
        sum += number
    return round(sum / len(list), 1)

print(return_average(grades_2))
    
#7 Write a recursive function to flatten a nested list.
def flatten_list(nested_list):
    flattened_list = []
    
    for checked_list in nested_list:
        if not isinstance(checked_list, list):
            flattened_list.append(checked_list)
        else:
            flattened_list.extend(flatten_list(checked_list))
    
    return flattened_list

print(flatten_list(nested_list_3))

#8 Implement a function that mimics the behavior of map()
def copy_map_functionality(list_to_transform):
    return list(map(to_upper, list_to_transform))

print(copy_map_functionality(names))