class InvalidAgeException(Exception):
    pass
try:
    age = int(input("Enter the value: "))
    if age < 18:
        raise InvalidAgeException("Age less than 18 is not allowed.")
    print("Age is valid.")
except InvalidAgeException as e:
    print(e)
