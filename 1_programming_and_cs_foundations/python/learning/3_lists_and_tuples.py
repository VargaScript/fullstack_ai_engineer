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










# Lists Exercises
import math
list1 = [4, 8, 15, 16, 23, 42, 15, 8, 4]
list2 = [23, 42, 50, 60, 70]
nested_list = [1, [2, 3], [4, [5, 6]], 7]
chunk_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
rotate_list = [1, 2, 3, 4, 5, 6, 7]
rotate_k = 3

#1. Sum all the elements in a list.
def sum_all_elements(list):
    return sum(list)

print(sum_all_elements(list1))

def sum_all_elements2(list):
    total_sum = 0
    for number in list: 
        total_sum += number
    return total_sum

print(sum_all_elements2(list1))

#2. Remove duplicates from a list.
def remove_duplicates(list):
    removed_list = []
    for number in list:
        if number in removed_list:
            continue
        else:
            removed_list.append(number)
    return removed_list

print(remove_duplicates(list1))

#3. Reverse a list manually (without reverse() or [::-1]).
def reverse_list(list1):
    reversed_list = []
    for item in range(1, len(list1) + 1): 
        reversed_list.append(list1[-item])
    return reversed_list

print(reverse_list(list1))

#4. Merge two lists and remove duplicates.
def merge_lists(list1, list2):
    merged_list = []
    merged_list.extend(list1)
    merged_list.extend(list2)
    
    clear_list = []
    for item in merged_list: 
        if item not in clear_list:
            clear_list.append(item)
        else: 
            continue
        
    return clear_list

print(merge_lists(list2, chunk_list))
    
#5. Find the second largest element in a list.
def second_largest(list1):
    list1.sort()
    
    return list1[-2]

print(second_largest(list1))

#6. Rotate a list to the right by k positions.
def rotate(rotate_list, positions):
    return print(rotate_list[-positions:] + rotate_list[:-positions])

rotate(rotate_list, rotate_k)

#7. Flatten a nested list.
def flatten_list(nested_list):
    flat_list = []
    
    for item in nested_list: 
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else: 
            flat_list.append(item)
        
    return flat_list

print(flatten_list(nested_list))   
 
#8. Chunk a list into smaller lists of size n.
def smaller_lists(chunk_list, length):
    new_list = []
    for item in range(0, len(chunk_list), length):
        new_list.append(chunk_list[item:item + length])
    return new_list

print(smaller_lists(chunk_list, 3))










# Tuples Exercises

tuple1 = (10, 20, 20, 30, 40, 50, 50, 50, 60)
tuple2 = (70, 80, 90)
tuple_list = [("Alice", 25), ("Bob", 30), ("Charlie", 20), ("David", 25)]
swap_tuple = (100, 200)
coordinates_dict = {
    (0, 0): "Origin",
    (1, 2): "Point A",
    (3, 5): "Point B",
    (-1, -1): "Point C"
}

#1. Convert a tuple to a list and back.
def convert_to_list_and_back(converted_tuple):
    convert_to_list = list(converted_tuple)
    convert_to_tuple = tuple(convert_to_list)
    return [convert_to_list, convert_to_tuple]

print(convert_to_list_and_back(tuple2))

#2. Access the last element of a tuple.
def last_element(access_tuple):
    last_tuple_element = access_tuple[-1][-1]
    return last_tuple_element

print(last_element(tuple_list))

#3. Count how many times an element appears in a tuple.
def count_element_tuple(tuple1, element):
    counter = tuple1.count(element)    
    return counter
    
print(count_element_tuple(tuple1, 50))

#4. Unpack a tuple into variables and swap values.
def unpack_and_swap(tuple1):
    first_element, second_element = tuple1
    swapped_tuple = second_element, first_element
    return swapped_tuple

print(unpack_and_swap(swap_tuple))

#5. Concatenate two tuples.
def concatenate_tuples(tuple1, tuple2):
    concatenated_tuples = tuple1 + tuple2
    return concatenated_tuples

print(concatenate_tuples(tuple1, tuple2))

#6. Sort a list of tuples by the second item in each tuple.
def sort_by_second_item(tuple_list):
     return sorted(tuple_list, key=lambda item: item[1])

print(sort_by_second_item(tuple_list))

#7. Create a function that returns multiple values as a tuple and destructure them cleanly.
def return_destructured_tuple(tuple_list):
    one, *two, three = tuple_list
    return one, two, three
    
print(return_destructured_tuple(tuple_list))

#8. Use tuples as dictionary keys to store coordinates and values.
def create_coordinates_tuples(coordinates):
    place_coordinates = ""
    for key, value in coordinates.items():
        place_coordinates += f"The place {value} is at the coordinates {key}\n"
    return place_coordinates

print(create_coordinates_tuples(coordinates_dict))