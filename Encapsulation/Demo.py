class Demo:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")
person = Demo("Gaurav", 23)
print(person.name)
person.name = "vivek" 
print(person.age)
person.age = 30
person.display_info()