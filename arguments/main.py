from typing import Tuple,Dict
from enum import Enum
# positional argument
# sum_all_numbers returns sum of all numbers passed as an arguments
def sum_all_numbers(*args:Tuple)->int:
    return sum(args)

print(sum_all_numbers(1,2,3,4,5,6))
    
# keyword arguments
# person_info prints person information
def person_info(**kwargs:Dict)->None:
    for k,v in kwargs.items():
        print(f"{k}:{v}")
        
# person_info(**{
#     "name":"Nitesh",
#     "age":28,
#     "profession": "Software Engineer",
# })

person_info(name="Nitesh",age=28,profession="SWE")

class CarType(Enum):
    HATCHBACK=0
    SEDAN=1
    XUV=2
    SPORTS=3
    LUXURY=4
    
class Car:
    """
        Car defines a car object with model type and name.
    """
    def __init__(self,name:str,car_type:CarType):
        self.type = car_type
        self.name = name
    
    def __repr__(self):
        return f"Car {self.name} is {self.type} type"

car = Car("Ford Fiesta",CarType.SEDAN)
print(car)

        
    