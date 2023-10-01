# Cars is iterator because it implements __next__
# Also Cars is iterables because it implements __iter__ 
class Cars:
    def __init__(self,car_names:list) -> None:
        self.cars_names:list = car_names
        self.index = -1
    
    # __next__ returns a value
    def __next__(self)->str:
        self.index +=1
        if self.index >= len(self.cars_names):
            raise StopIteration
        else:
            return self.cars_names[self.index]
    def __iter__(self):
        return self

class CarIterables:
    
    def __init__(self,car_iterators:Cars) -> None:
        self.car_iter = car_iterators
    
    # __iter__ implements object of an iterator class 
    def __iter__(self):
        return self.car_iter

car_names = ["AVC","HYUNDAI","MG"]
cars = Cars(car_names)
print(list(cars))
print(cars.index)
# print(next(cars))
# print(next(cars))
# print(next(cars))
# print(next(cars))

# car_iterables = CarIterables(cars)
for car in cars:
    print(car)