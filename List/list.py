from typing import List
a:List = [1,2,5,7,12,9,-1]
print(len(a)) # 7
print(a)
print(id(a))
a.append(7)
print(a)
print(id(a))
arr:list = a[::]
print(id(arr))

# Note : append usually doesn't create a new list 
# it only adds element at the end of existing list if capacity is reached
# then it will copy each element of existing list to a new list of double length
# append, TC: amortized O(1)

print(a)
print(id(a))
a.remove(12)# O(N)
a.remove(7) # remove removes first ocurrence
print(id(a)) # remove happens on the same list
print(a)

# Question: Given a list write a function to remove element at any 
# given index

# Question: Given a list write a function to insert element at any 
# given index

a.sort()
print(a)

print(a)

a.reverse()
print(a)






