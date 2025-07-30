#Exercises

number = 27

a = 34
b = 12
c = 78

age = 17

score = 86

year = 2024

string1 = "apple"
string2 = "banana"

stored_username = "admin"
stored_password = "1234"
input_username = "admin"
input_password = "1234"

temperature = 30
is_raining = True

#1. Check if a number is even or odd.
def check_odd_number(number):
    if number % 2 != 0:
        return f"The number {number} is odd"
    return f"The number {number} is even"

print(check_odd_number(number))

#2. Find the greatest of three numbers.
def find_greatest_number(number1, number2, number3):
    if number1 > number2 and number1 > number3:
        return f"The greatest number is {number1}"
    elif number2 > number1 and number2 > number3:
        return f"The greatest number is {number2}"
    elif number3 > number1 and number3 > number2:
        return f"The greatest number is {number3}"
    else: 
        return "There's a draw between numbers!"
    
print(find_greatest_number(a, b, c))

#3. Determine if a person is eligible to vote.
def is_voting(age):
    return True if age >= 18 else False
    
print(is_voting(age))
    
#4. Write a grading system based on a score input.
def grades(calif):
    if calif >= 90 and calif <= 100:
        return f"You have an 'A'"
    elif calif >= 80 and calif < 90:
        return f"You have a 'B'"
    elif calif >= 70 and calif < 80:
        return f"You have a 'C'"
    elif calif >= 60 and calif < 70:
        return f"You have a 'D'"
    elif calif > 100:
        return f"This is impossible!"
    else:
        return f"You've failed!"
    
print(grades(score))

#5. Determine if a year is a leap year.
def find_leap_year(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

print(find_leap_year(year))

#6. Compare two strings alphabetically (lexicographically).
def compare_lexico(string1, string2):
    if string1 < string2:
        return f"{string1} comes first than {string2} on the alphabet"
    else:
        return f"{string2} comes first than {string1} on the alphabet"

print(compare_lexico(string1, string2))

#7. Simulate a basic login system with username and password.
def login(stored_username, stored_password, input_username, input_password):
    
    if stored_username == input_username and stored_password == input_password:
        return "Login success"
    else:
        return "Try again"
        
print(login("w", stored_password, input_username, input_password))

#8. Implement a simple decision-making tree with nested conditionals.
def decision_tree(temp, rain):
    if temp > 30:
        if rain is not True:
            return "It's too hot and it's not raining. Put yourself on some sun blocker"
        else:
            return  "It's a little bit hot but it's raining. Get your umbrella"
    else:         
        return "It's charming outside, enjoy your world"        

print(decision_tree(temperature, is_raining))