from typing import List 
import functools

# reduce will return a single element out of list
a:List = [1,2,3,4,5,6,7,8,9]

def sum(curr,total):
    return total+curr

# print(functools.reduce(sum,a,2))
print(functools.reduce(lambda curr,total:curr+total,a))



