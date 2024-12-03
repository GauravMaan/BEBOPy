# Positional and Keyword Arguments in Python Functions

# Positional Arguments:
# These are arguments passed to a function in the order in which the function's parameters are defined.
# The position of the argument matters, and values are assigned to parameters based on their order.

# Keyword Arguments:
# These are arguments passed to a function by explicitly specifying the parameter name along with its value.
# The order of arguments does not matter when using keyword arguments.

def person(name, age, city="Unknown"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
person("Alice", 25, "New York")
person("Bob", 30, city="Los Angeles")
person(age=35, name="Charlie", city="San Francisco")
