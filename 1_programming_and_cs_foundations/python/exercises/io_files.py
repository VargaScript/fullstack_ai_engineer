import os

print(os.getcwd())

with open(r"1_programming_and_cs_foundations/python/exercises/tale.txt", "r") as tale:
    for line in tale:
        print(line.strip())
        
        
with open("1_programming_and_cs_foundations/python/exercises/hello_world.txt", "w") as hello:
    hello.write("Hello World!")