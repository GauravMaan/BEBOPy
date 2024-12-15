class Grandparent:
    def say_hello(self):
        return "Hello from Grandparent!"
class Parent(Grandparent):
    def say_hello_parent(self):
        return "Hello from Parent!"
class Child(Parent):
    def say_hello_child(self):
        return "Hello from Child!"
child = Child()
print(child.say_hello())
print(child.say_hello_parent())
print(child.say_hello_child())