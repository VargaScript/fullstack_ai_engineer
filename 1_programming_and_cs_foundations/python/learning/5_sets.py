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
#.symmetric_difference_update(): Inserts the symmetric differences from this set and another.
union = set_b.union(set_c)                           # {"banana", "kiwi", "orange"}
update = set_b.update(set_c)                         # {"banana", "kiwi", "orange"} (This is the new content of set b)









#Exercises

#1. Remove duplicates from a list using a set.

#2. Check if two sets have common elements.

#3. Add a new item to a set.

#4. Find the symmetric difference between two sets.

#5. Check if a set is a subset or superset of another.

#6. Remove an element from a set only if it exists.

#7. Given a list of words, return all unique characters across all words.

#8. Implement a function that returns the difference of multiple sets.