from typing import List

a:List=[1,2,3,4,5,6,7,8,9]

def is_even(num:int)->bool:
    return num%2==0

# print((lambda num:num%2==0)(5))

#filtered_list:List = filter(is_even,a)
#print(list(filtered_list))

filtered_list:List = filter(lambda num:num%2==0,a)
print(list(filtered_list))

