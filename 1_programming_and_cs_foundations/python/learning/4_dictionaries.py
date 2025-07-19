student = {
    "first_name": "Adair",
    "last_name": "Vargas",
    "age": 23,
    "email": "adair@example.com",
    "grades": [90, 85, 92],
    "enrolled": True,
    "address": {
        "city": "Mexicali",
        "country": "Mexico"
    }
}


student.clear()                             # {}
print(student) 

student = {
    "first_name": "Adair",
    "last_name": "Vargas",
    "age": 23,
    "email": "adair@example.com",
    "grades": [90, 85, 92],
    "enrolled": True,
    "address": {
        "city": "Mexicali",
        "country": "Mexico"
    }
}

copy = student.copy()                                           # {'first_name': 'Adair', 'last_name': 'Vargas', 'age': 23, 'email': 'adair@example.com', 'grades': [90, 85, 92], 'enrolled': True, 'address': {'city': 'Mexicali', 'country': 'Mexico'}}
print(copy)
key = ["first_name", "age", "enrolled"]
fromkeys = student.fromkeys(key, "")                           # {'first_name': ['Christian', 43, False], 'age': ['Christian', 43, False], 'enrolled': ['Christian', 43, False]}
print(fromkeys)
get = student.get("age")                                        # 23
print(get)
items = student.items()                                         # dict_items([('first_name', 'Adair'), ('last_name', 'Vargas'), ('age', 23), ('email', 'adair@example.com'), ('grades', [90, 85, 92]), ('enrolled', True), ('address', {'city': 'Mexicali', 'country': 'Mexico'})])
print(items)
keys = student.keys()                                           # dict_keys(['first_name', 'last_name', 'age', 'email', 'grades', 'enrolled', 'address'])
print(keys)
pop = student.pop("first_name")                                 # "Adair"
print(pop)
popitem = student.popitem()                                     # ('address', {'city': 'Mexicali', 'country': 'Mexico'})
print(popitem)
setdefault = student.setdefault("income", 19000)                # 19000
print(setdefault)
update = student.update({"first_name": "Dhayana"})              # None
print(update)
values = student.values()                                       # dict_values(['Vargas', 23, 'adair@example.com', [90, 85, 92], True, 19000, 'Dhayana'])
print(values)


for key, value in student.items():
    print(key, " ", value)
    
    
    
    
    
    
    
    
    
    
# Exercises

keys = ["age", "name", "height"]
values = ["21", "Adair", "1.78"]
user = {
    "username": "johndoe",
    "email": "john@example.com"
}
book = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949
}
countries = {
    "USA": "Washington",
    "France": "Paris",
    "Japan": "Tokyo"
}
dict_a = {"a": 1, "b": 2}
dict_b = {"c": 3, "d": 4}
text = "data science"
words = ["apple", "banana", "cherry", "avocado", "blueberry", "carrot"]
grades = {
    "Alice": {"Math": 90, "English": 85},
    "Bob": {"Math": 75, "English": 95},
    "Charlie": {"Math": 88, "English": 79}
}

#1. Create a dictionary with 3 key-value pairs.
def create_dict(keys, values):
    return dict(zip(keys, values))

print(create_dict(keys, values))

#2. Access a value safely using .get() without raising an error.
def access_value(dictionary, value):
    return dictionary.get(value)

print(access_value(user, "email"))

#3. Iterate through keys and values.
def iterate_through_items(dictionary):
    
    for item in dictionary:
        for key, value in dictionary.items():
            print(f"Hola {key} {value}")

iterate_through_items(book)
#4. Invert a dictionary (swap keys and values).

#5. Merge two dictionaries.

#6. Count frequency of each character in a string and store in a dict.

#7. Group words by their first letter into a dictionary.

#8. Create a nested dictionary to represent student grades per subject.