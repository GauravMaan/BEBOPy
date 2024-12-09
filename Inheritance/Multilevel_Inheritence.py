class A:
    x,y=10,20
    def m1(self):
       print(self.x+self.y)
class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)
class C(B):
    i,j=10,2002
    def m3(self):
        print(self.i+self.j)
Cob=C()
Cob.m2()
Cob.m1()
Cob.m3()