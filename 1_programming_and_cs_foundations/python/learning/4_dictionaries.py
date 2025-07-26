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
grades_data = [
    ("Alice", "Math", 88),
    ("Alice", "Science", 92),
    ("Alice", "English", 85),
    ("Bob", "Math", 76),
    ("Bob", "Science", 81),
    ("Bob", "English", 79),
    ("Charlie", "Math", 93),
    ("Charlie", "Science", 89),
    ("Charlie", "English", 90),
    ("Diana", "Math", 85),
    ("Diana", "Science", 87),
    ("Diana", "English", 82),
    ("Ethan", "Math", 91),
    ("Ethan", "Science", 90),
    ("Ethan", "English", 88),
]

import collections

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
    
    print(f"The book {dictionary["title"]} written by {dictionary["title"]} was written in {dictionary["year"]}")
  
iterate_through_items(book)

#4. Invert a dictionary (swap keys and values).
def swap_dict(dictionary):
    swapped_dictionary = {}
    
    for key, value in dictionary.items():
        swapped_dictionary[value] = key
    return swapped_dictionary
    
print(swap_dict(countries))
    
#5. Merge two dictionaries.
def merge_dicts(dict1, dict2):
    merged_dict = {}
    dict1 = list(dict1.items())
    dict2 = list(dict2.items())
    arr = dict1 + dict2
    
    for item in arr:
        key = item[0]
        value = item[1]
        merged_dict[key] = value
    return merged_dict

print(merge_dicts(dict_a, dict_b))

#6. Count frequency of each character in a string and store in a dict.
def count_char(string):
    char_count = {}
    
    for letter in string:
        if letter not in char_count:
            char_count[letter] = 1
        else: 
            char_count[letter] += 1
    
    return char_count
    
print(count_char(text))

#7. Group words by their first letter into a dictionary.
def group_words(words):
    normalized_words = []
    
    for word in words:
        normalized_word = word.lower()
        normalized_words.append(normalized_word)
    
    words_by_first_letter = {}
    for word in normalized_words:
        if word[0] not in words_by_first_letter:
            words_by_first_letter[word[0]] = [word]
        else: 
            words_by_first_letter[word[0]] += [word]
    
    return words_by_first_letter

print(group_words(words))

#8. Create a nested dictionary to represent student grades per subject.
def nested_dict(grades):
    student_dict = {}
    
    for student, subject, score in grades:
        if student not in student_dict:
            student_dict[student] = {}
        student_dict[student][subject] = score
        
    return student_dict
 
print(nested_dict(grades_data))