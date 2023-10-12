from enum import Enum

class CarType(Enum):
    HATCHBACK=0
    SEDAN=1
    SUV=2
    SPORTSCAR=3
    

class Car:
    def __init__(self,car_type:CarType,id:int) -> None:
        self.car_type = car_type
        self.id=id
    
    def __str__(self):
        return f"Car type for {self.id} car object is {self.car_type}"
    
    def __and__(self,obj):
        return self.id & obj.id  
    
    def __or__(self,obj):
        return self.id | obj.id

car1 = Car(CarType.HATCHBACK,1)
print(car1)

car2 = Car(CarType.SPORTSCAR,2)
print(car2)

print(car1 & car2)
print(car1 | car2)

print(None and car2)

print(car1 or car2)



# if car1.car_type == CarType.HATCHBACK:
#     print("hatch type car object")
        
        