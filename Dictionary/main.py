from typing import Dict,List,Any

# Dictionary

my_dict:Dict = {
    #"1":123,
    3:112,
    #(1,2,3):"7",
    #[1,2,3]:9,
    #{}:{}
}
print(id(my_dict))

def modify(my_list:List):
    my_list.append(1)
    

def print_dict(my_dictionary:Dict[int])->None:
    #count=[]
    #modify(count)
    #print(count)
    print(id(my_dictionary))
    for k,v in my_dictionary.items():
        print(f"{k}:{v}")
print_dict(my_dict)

#my_dictionary = my_dict
#print(my_dict["Hello"])
#print(my_dict.get("Hello"))
# if my_dict.get("something")!=None:
#     pass
# else:
#     raise KeyError("Key Error")
my_dict.__setitem__("34",112)
print(my_dict)

#kwargs










