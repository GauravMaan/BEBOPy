import sys
sys.path.append("/Users/gauravmaan/Desktop/BEBOPy/Packages/FirstPack")
sys.path.append("/Users/gauravmaan/Desktop/BEBOPy/Packages/FirstPack/SecondPack")
sys.path.append("/Users/gauravmaan/Desktop/BEBOPy/Packages/ThirdPack")

from Emp import *
obj1=emp()
obj1.emo()

from emp1 import *
obj2=Emp1()
obj2.emo("gaurav")

import Demo
Demo.add(2,4)
import Animal1
Animal1.fly()
import Animal
Animal.walk()
