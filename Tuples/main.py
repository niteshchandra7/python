from typing import Tuple,List
# Tuples
# Tuples can hold data of multiple types but 
# it(tuple) can not be changed after it is created
t:Tuple = (1,2,3,4,5)
t:Tuple = 1,2,3,4,5 
print(type(t))

for (k,v) in enumerate(t): # k,v together forms a tuple
    print(f"key: {k}, value: {v}")
    
#new_t:Tuple = 1,
new_t:Tuple = (1,)
print(type(new_t))

#(a,b) = (1,2)

print(t[1])
#t[1]=4 # ilegal operation, 'tuple' object does not support item assignment

for elem in t:
    print(elem)
    
print(3 in t) # O(N)

sliced_t:Tuple = t[3:] # slicing in tuple is allowed
print(sliced_t) 

print(len(t))
#print(t.count(19)) #O(N)

# positional arguments

def sum_all_numbers(*args): # args is packed to tuple
    #print(type(args)) # tuple
    #return sum(args)
    sum=0
    for elem in args:
        sum+=elem
    return sum
    



print(sum_all_numbers(*(1,2,3,4))) # tuple is getting unpacked to positional arguments (1,2,3,4) 
print(sum_all_numbers(1,2,3))

print(sum_all_numbers(*t))

print(int(2/3))
