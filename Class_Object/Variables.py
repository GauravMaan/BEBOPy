#global
#local
#instance /class variable

# class MyVar:
#     a,b=10,20
#     def sum(self):
#         print(self.a+self.b)
#     def sub(self):
#         print(self.a-self.b)
# obj1=MyVar()
# obj1.sum()
# obj1.sub()

# class MyVar1:
#     a,b=10,20
#     def sum(self,x,y):
#         print(x+y)
#         print(self.a+self.b)
#
# obj1=MyVar1()
# obj1.sum(1,2)

# i,j=20,30                                     #global
# class MyVar2:
#     a,b=10,20                                 # Instance
#     def sum(self,x,y):                        # local
#         print(x+y)
#         print(self.a+self.b)
#         print(globals()['i']+globals()['j'])
#
# obj1=MyVar2()
# obj1.sum(1,2)


x = 100
class Example:
    def variables(self,y):
        print(globals()['x'])
        print(y)
obj = Example()
obj.variables(200)