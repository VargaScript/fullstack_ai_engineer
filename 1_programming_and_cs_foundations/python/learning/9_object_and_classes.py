#Exercises
name_1 = "Adair"
age_1 = 23
🔹 #2 Add a method to greet from the Person class.
Same person data from above:

python
Copiar
Editar
# Reuse:
name_1 = "Adair"
age_1 = 23
🔹 #3 Create two instances and print their attributes.
Use:

python
Copiar
Editar
name_2 = "Luisa"
age_2 = 30
🔹 #4 Create a Student class that inherits from Person and adds GPA.
Use:

python
Copiar
Editar
student_name = "Carlos"
student_age = 20
student_gpa = 3.85
🔹 #5 Use __str__ to make your class printable.
Reuse any of the previous instances (e.g., Carlos or Luisa) — just make sure when you print(student) or print(person) it returns something nice.

🔹 #6 Use a class attribute to count how many instances have been created.
Create multiple instances:

python
Copiar
Editar
person_1 = ("Adair", 23)
person_2 = ("Luisa", 30)
person_3 = ("Daniel", 28)
person_4 = ("María", 19)
🔹 #7 Implement a BankAccount class with deposit(), withdraw(), and balance tracking.
Use:

python
Copiar
Editar
account_holder = "Adair"
initial_balance = 1500.0

transactions = [
    ("deposit", 500.0),
    ("withdraw", 200.0),
    ("deposit", 1200.0),
    ("withdraw", 300.0)
]
🔹 #8 Design a simple inventory system with classes Product, Category, and Cart.
Use:

python
Copiar
Editar
products = [
    {"name": "Laptop", "price": 1200.0, "category": "Electronics"},
    {"name": "Headphones", "price": 150.0, "category": "Electronics"},
    {"name": "Notebook", "price": 5.0, "category": "Stationery"},
    {"name": "Pen", "price": 2.0, "category": "Stationery"}
]

cart_operations = [
    {"product_name": "Laptop", "quantity": 1},
    {"product_name": "Notebook", "quantity": 3},
    {"product_name": "Pen", "quantity": 5}
]


#1 Create a class Person with name and age attributes.

#2 Add a method to greet from the Person class.

#3 Create two instances and print their attributes.

#4 Create a Student class that inherits from Person and adds GPA.

#5 Use __str__ to make your class printable.

#6 Use a class attribute to count how many instances have been created.

#7 Implement a BankAccount class with deposit/withdraw and balance tracking.

#8 Design a simple inventory system with classes Product, Category, and Cart.