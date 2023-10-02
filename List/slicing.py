# List slicing

arr:list=[0,1,2,3,4,5,6,7,8,9]
# start - will start from this index
# stop - will stop at this index but won't include
# step - for each iteration how much to move
# step can be negative as well as positive

arr_new:list=arr[1:20:2]
print(arr_new)

arr_new = arr[1:5:1]
print(arr_new)
arr_new[0]= -1
print(arr_new)
print(arr)

arr_new = arr
arr_new[0]=-1
print(arr)

# Note: slicing creates a copy

arr1 = arr  # O(1)
arr2 = arr[::] # O(N)

string:str = "Hello, Riya"

string1:str = string[0:6:1]
print(string1)

a:list = "Hello,Riya".split(',') # split splits a string into list for given seperator
print(a)
alpha = " ".join(["Riya","Nitesh","Rohith"]) # join joins a list of string with given separator
print(alpha)

