class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
        print(f"Total number of objects created: {Counter.count}")
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

