# import math
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def distance(self, point):
#         dist = math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)
#         return dist
# point1 = Point(3, 4)
# point2 = Point(7, 1)
# dist = point1.distance(point2)
# print(dist)
import math
class Point:
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def distance(self):
        x=self.x2-self.x1
        y=self.y2-self.y1
        result=math.sqrt((x*x)+(y*y))
        print(result)
p1=Point(3,7,4,1)
p1.distance()