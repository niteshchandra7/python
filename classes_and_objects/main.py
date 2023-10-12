# OOPs

# A - Abstraction 
    # We only show those methods and attributes which is needed for client
    # _fun (protected)
    # __fun (private)
# P - Polymorphism
    # compile time polymporphism/function overloading is not supported by python
    # def add(num1:float,num2:float)
    # def add(num1:int,num2:int)
    
    # Run time Polymorphism:
        # Method will be called of calling object


# I - Inheritance
    # Is-a relationship, Riya is a person, class Riya can inherit from person
    # Has-a relationship, Riya has spectacles, Riya class has spectacle
    # class Spectacle:
    #    pass
    
    # class Person:
    #    def sound():
    #        return f"Gibber Jabber"
    
    # class Riya(Person):
    #    def __init__(self, spectacle:Spectacle):
    #         super().__init__(self)
    #        self.spectacle = spectacle
    #    def sound():
    #        super().sound()
    #        return f"Aww Awwww"
    # persons:List[Person] = [riya,person,spectacle] # List of objects
    # for person in range(persons):
    #    print(person.sound())
# E - Encapsulation
    # attribute and method are encapsulated


# def add(num1:int,num2:int):
#     print(f"int type")
#     return int(num1+num2)

# def add(num1:float,num2:float,num3:float):
#     print(f"float type")
#     return num1+num2+num3

# print(add(1.2,2.2))
# print(add(1,2))




from abc import ABCMeta,abstractmethod

class Bird(ABCMeta):
    
    @classmethod
    def set_object_count(cls,count):
        cls.count=count
        
    @classmethod
    def get_object_count(cls):
        return cls.count
        
    
    @abstractmethod # abstact method is relevant only when class inherits from ABCMeta 
    def make_sound():
        pass
        
    @abstractmethod
    def fly():
        pass
    
    @staticmethod
    def greet():
        print("Hello")
    
# bird = Bird()
# print(bird)


Bird.set_object_count(0)
# created an object
Bird.set_object_count(Bird.get_object_count()+1)
print(Bird.get_object_count())
Bird.greet()
