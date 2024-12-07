class Counter:
    count = 0
    def m1(self):
        Counter.count += 1
        print(f"Total number of objects created: {Counter.count}")
obj1 = Counter()
obj1.m1()
obj2 = Counter()
obj2.m1()
obj3 = Counter()
obj3.m1()
