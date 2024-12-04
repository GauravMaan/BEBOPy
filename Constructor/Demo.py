#constractor name is fixed def __init__(self)
#it will not return any value
#it can also receive the arguments and parameter
#it is called automatically when obj is created


# In Python, a constructor is a special method used to initialize the attributes of an object when the object is created. This method is named __init__() and is automatically called when an object of the class is instantiated.
#
# Key Points about Constructors:
#
# 	1.	Purpose: The constructor is used to assign initial values to the instance variables of a class.
# 	2.	Special Name: The constructor method is always named __init__ and must have at least one parameter (self), which refers to the instance being created.
# 	3.	Default Constructor: If a class doesn’t define a constructor, Python provides a default constructor that doesn’t perform any initialization.
# 	4.	Parameterized Constructor: A constructor can take parameters to initialize attributes with specific values.

# class demo:
#     def __init__(self):
#         print("hello")
#     def demo1(self):
#         print("world")
# obj1=demo()
# obj1.demo1()

class demo:
    def __init__(self):
        print("hello")
    def demo1(self):
        print(self) # for address of class object
obj1=demo()
obj1.demo1()

# # __str__()=it is use to define the string representation of an obj
# class myclass:
#     def __str__(self):
#         return "hello"
# onj1=myclass()
# print(onj1)