#we can call them directly
#Static does not take self parameter.because it is not bound with an instance
class MyClass():
    def m1(self):
        print("today is beautiful day")
    @staticmethod
    def m2(num):
        print(num)
obj1=MyClass()
obj1.m1()
MyClass.m2(5)
