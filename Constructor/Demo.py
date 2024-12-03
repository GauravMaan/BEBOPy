#constractor name is fixed def __init__(self)
#it will not return any value
#it can also receive the arguments and parameter
#it is called automatically when obj is created

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