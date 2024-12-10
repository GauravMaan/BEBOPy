from abc import ABC, abstractmethod
class a(ABC):
    @abstractmethod
    def m1(self):
        pass
class b(a):
    def m1(self):
        print("m1 implemented in b")
    def m2(self):
        print("gaurav")
class c(b):
    def m3(self):
        print("maan")
obj1 = c()
obj1.m1()
obj1.m2()
obj1.m3()