from typing import List
# Map
arr:list=[1,2,3,4,5] # exp 2,4,6,8,10
print(list(map(lambda x: x*2, arr))) # 2,4,6,8,10

# Filter
print(list(filter(lambda x:x%2==0,arr))) # 2,4

# Reduce
import functools
print(functools.reduce(lambda curr,total:total+curr,arr,0)) # 15

# any
print(any(arr)) # checks whether any item in list is true
# all
print(all(arr)) # checks whether all item in list is true

arr[0]=0
print(arr)
print(any(arr))
print(all(arr))

# lambda function

def add(x:int,y:int)->int:
    return x+y

print(add(2,5))

print((lambda x,y:x+y)(2,5))

names:List[str] = ["riya", "nitesh", "baua"]

# ["Riya", "Nitesh", "Baua"]

# title converts name to Title type name
def title(elem:str)->str:
    return elem.title()

map1 = map(title,names) # m is an iterator
print(list(map1))
# print(next(m))

map2 = map(lambda elem:elem.title(),names)
print(list(map2))











