#Exercises

# Use range()

numbers = [5, 12, 8, 3, 10, 7]

user_profile = {
    "name": "Adair",
    "age": 23,
    "email": "adair@example.com",
    "city": "Mexicali"
}

number = 7

# Use range()

n = 50

secret_number = 17

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


#1 Print numbers from 1 to 10 using a loop.
def generate_number_range(first_number, last_number):
    for number in range(first_number, last_number + 1):
        print(number)

generate_number_range(5, 69)

#2 Sum all numbers in a list with a for loop.
def sum_all_numbers(number_list):
    total_number = 0
    
    for number in number_list:
        total_number += number
    
    return total_number 

print(sum_all_numbers(numbers))

#3 Iterate over a dictionary and print keys and values.
def print_keys_and_values(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

print_keys_and_values(user_profile)
    
#4 Create a multiplication table for a number.
def multiplication_table(multiplied_number):
    for number in range(1, 10 + 1):
        result = multiplied_number * number
        print(f"{multiplied_number} x {number} = {result}")

multiplication_table(number)

#5 Find all even numbers between 1 and 100.
def even_numbers_to_100():
    for number in range(1, 100 + 1):
        if number % 2 == 0:
            print(number)

even_numbers_to_100()

#6 Generate a list of prime numbers up to n.
def prime_numbers(limit):
    primes = []
    
    for number in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes

print(prime_numbers(n))

#7 Build a number-guessing game with a loop.
def guess_number(machine_number):
    
    while True:
        user_guess = int(input("Type a number to guess: ").strip())
        
        if machine_number == user_guess:
            print("Congrats, you found the number!")
            break
    
guess_number(secret_number)

#8 Loop through a nested list and print each element.
def print_nested_list(matrix):
    for row in matrix:
        for item in row:
            print(item)

print_nested_list(matrix)