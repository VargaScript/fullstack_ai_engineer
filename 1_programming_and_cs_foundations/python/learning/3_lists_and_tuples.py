my_list = ["Adair", "Isai", "Vargas", "Pastrana", "Adair"]

append = my_list.append(["Dhayana", "Christian"])        # ["Adair", "Isai", "Vargas", "Pastrana", "Adair", ["Dhayana", "Christian"]]
print(my_list)
clear = my_list.clear()                                  # []
print(my_list)
my_list = ["Adair", "Isai", "Vargas", "Pastrana", "Adair"]
copy = my_list.copy()                                    # ["Adair", "Isai", "Vargas", "Pastrana", "Adair"] (But in a new memory pointer)
print(my_list)
count = my_list.count("Adair")                           # 2
print(count)
extend = my_list.extend(["Dhayana", "Christian"])        # ["Adair", "Isai", "Vargas", "Pastrana", "Adair", "Dhayana", "Christian"]
print(my_list)         
index = my_list.index("Christian")                       # 6
print(index)    
insert = my_list.insert(3, "Monserrat")                  # ["Adair", "Isai", "Vargas", "Monserrat", "Pastrana", "Adair", "Dhayana", "Christian"]
print(my_list)                
pop = my_list.pop()                                      # ["Adair", "Isai", "Vargas", "Monserrat", "Pastrana", "Adair", "Dhayana"]
print(my_list)
remove = my_list.remove("Monserrat")                     # ["Adair", "Isai", "Vargas", "Pastrana", "Adair", "Dhayana"]
print(my_list)
reverse = my_list.reverse()                              # ["Dhayana", "Adair", "Pastrana", "Vargas", "Isai", "Adair"]
print(my_list)
sort = my_list.sort()                                    # ["Adair", "Adair", "Dhayana", "Isai", "Pastrana", "Vargas"] 
print(my_list)

# Due to tuples don´t have much methods, it´s recommended to turn it into a list, 
# apply list methods and then turn it back to tuple
my_tuple = ("Adair", "Isai", "Vargas", "Pastrana", "Adair")

# Convert to list and modify
to_list = list(my_tuple)
to_list.append(["Christian", "Dhayana", "Monserrat"])
to_list.reverse()
to_tuple = tuple(to_list)

print(to_tuple)
print(my_tuple.count("Adair"))
print(my_tuple.index("Isai"))