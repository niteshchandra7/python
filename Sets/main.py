from typing import Set
# Sets
# Initialisation

set1:Set = set()
print(type(set1))

set2:Set = {None}#len is 1
print(len(set2))
set3:Set = {""} # len is 1
print(len(set3))
print(type(set2))

# fruits

fruits:Set = {"Jackfruit", "Banana","Guava","Apple"} # O(L*N)
print(fruits)
vegetables:Set = {"Potato","Jackfruit","Banana","Onion"}
print(vegetables)

#add
vegetables.add("lady-finger")
print(vegetables)

#remove
vegetable:str = "lady-finger1"
# if vegetable in vegetables:
#     vegetables.remove(vegetable)

try:
    vegetables.remove(vegetable)
except KeyError:
    print(f"WARNING: {vegetable} not found")    


#intersection. symmetric operation
print(fruits.intersection(vegetables)) 
print(vegetables.intersection(fruits))

# difference
print(fruits.difference(vegetables)) # Guava Apple
print(vegetables.difference(fruits)) # Potato Onion

# symmetric_difference
print(fruits.symmetric_difference(vegetables))
print(vegetables.symmetric_difference(fruits))

# union
print(fruits.union(vegetables))

# find
print("Potato" in vegetables)

# iterable
for vegetable in vegetables:
    print(vegetable)

# iterator
print(list(vegetables))
print(list(vegetables))

# copy
veggies:Set = vegetables.copy()
print(id(vegetables))
print(id(veggies))

#update is basically an inplace union
vegetables.update(fruits)
print(vegetables)



    



#  5 1 2 3 4 7 73 112 121

# hash function (x)%7 #O(N)

# 0 7 112
# 1 1
# 2 2 121
# 3 3 73 
# 4 4
# 5 5 
# 6
# 7
# 8

# B
# N
# O(N/B) # provided good hash code
# Linear Probing, Quadratic probing, Open Chaining



