set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "kiwi", "orange"}
set_c = {"banana", "cherry"}
empty_set = set()
set_clear = {"heollo"}

add = set_a.add("durazno")                          # {"apple", "banana", "cherry", "durazno"}
print(set_a)
clear = set_clear.clear()                           # {}
print(set_clear)
copy = set_b.copy()                                 # {"banana", "kiwi", "orange"}
print(copy)
difference = set_a.difference(set_b)                # {"apple", "cherry", "durazno"}
print(set_a)
difference_update = set_a.difference_update(set_b)  # {"apple", "cheery", "durazno", "orange", "kiwi"}
print(set_a)
discard = set_a.discard("orange")                   # {"apple", "banana", "cherry"}
print(set_a)
intersection = set_a.intersection(set_c)            # {"banana", "cherry"} 
print(set_a)                    
#.intersection_update(): Removes the items in the first set that are not present in the other.
#.isdisjoint(): Returns if two set have an intersection or not.
issubset = set_c.issubset(set_a)                    # True
print(set_c)
issuperset = set_a.issuperset(set_c)                # True
print(set_a)
pop = set_a.pop()                                   # Not really a specific return, it deletes one random item
print(set_a)
remove = set_c.remove("cherry")                     # {"banana"}
print(set_c)
#.symmetric_difference(): Returns a set with the symmetric differences between two sets.

                                                    # Return the different items between 2 sets without the ones that are on both sets
#.symmetric_difference_update(): Inserts the symmetric differences from this set and another.
union = set_b.union(set_c)                           # {"banana", "kiwi", "orange"}
update = set_b.update(set_c)                         # {"banana", "kiwi", "orange"} (This is the new content of set b)









#Exercises

numbers = [3, 5, 2, 3, 7, 2, 5, 9, 10, 3]

set_a = {"apple", "banana", "cherry", "date"}
set_b = {"kiwi", "banana", "mango", "date"}

colors = {"red", "green", "blue"}
new_color = "purple"

group1 = {"Anna", "Ben", "Claire", "Diana"}
group2 = {"Ben", "Diana", "Ethan", "Fiona"}

frontend = {"HTML", "CSS", "JavaScript"}
fullstack = {"HTML", "CSS", "JavaScript", "Python", "SQL"}

cities = {"London", "New York", "Paris", "Tokyo", "Berlin"}
to_remove = "Berlin"

words = ["data", "science", "python", "sets"]

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3}
set3 = {1, 5}

#1. Remove duplicates from a list using a set.
def remove_list_dupes(list_numbers):
    return set(list_numbers)

print(remove_list_dupes(numbers))

#2. Check if two sets have common elements.
def check_intersection(set1, set2):
    return set1.intersection(set2)    

print(check_intersection(set_a, set_b))

#3. Add a new item to a set.
def add_new_item(colors_list, new_item):
    colors_list.add(new_item)
    return colors_list

print(add_new_item(colors, new_color))

#4. Find the symmetric difference between two sets.
def symm_diff(set1, set2):
    return set1.symmetric_difference(set2)

print(symm_diff(group1, group2))

#5. Check if a set is a subset or superset of another.
def check_subset(set1, set2):
    if set1.issubset(set2):
        return f"{set1} is a subset of {set2}"
    return f"{set1} is not a subset of {set2}"

def check_superset(set1, set2):
    if set1.issuperset(set2):
        return f"{set1} is a superset of {set2}"
    return f"{set1} is not a superset of {set2}"

print(check_subset(frontend, fullstack))
print(check_superset(fullstack, frontend))

#6. Remove an element from a set only if it exists.
def remove_if_exists(set_to_check, element):
    if element in set_to_check:
        set_to_check.discard(element)
        return f"The city {element} does exist on the set. Now it is removed"
    return f"The city {element} does not exist on the set"

print(cities)
print(remove_if_exists(cities, to_remove))
print(cities)

#7. Given a list of words, return all unique characters across all words.
def unique_characters_list(words):
    unique_char_set = set()
    
    for word in words:
        for char in word:
            if char not in unique_char_set:
                unique_char_set.add(char)
    return unique_char_set
    
#   return {char for word in words for char in word}
    
print(unique_characters_list(words))

#8. Implement a function that returns the difference of multiple sets.
def difference_multiple_sets(*sets):
    if not sets:
        return set()
    result = sets[0]
    for s in sets[1:]:
        result = result.difference(s)
    return result

print(difference_multiple_sets(set1, set2, set3))