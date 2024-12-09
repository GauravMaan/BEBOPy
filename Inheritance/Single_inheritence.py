# class A:
#     def __init__(self):
#         print("i am iron man")
#     def m1(self):
#         print("hi")
# class B(A):
#     def __init__(self):
#         print("i am batman")
#     def m2(self):
#         print("Yoo")
# Bobj=B()
# Bobj.m2()
# Bobj.m1()
# Aobj=A()
class A:
    x,y=10,20
    def m1(self):
       print(self.x+self.y)
class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)
Bobj=B()
Bobj.m2()
Bobj.m1()