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