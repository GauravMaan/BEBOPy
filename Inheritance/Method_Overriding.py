class A:
    def m1(self):
       print("i Am speed")
class B(A):
    def m1(self):
        print("I am not speed i am boost")
        super().m1() #invoke immediate parent class method ; calling parent class
obj1=B()
obj1.m1()