# Purpose of a return Statement:
# The return statement in a function is used to send the result of the function back to the caller.
# It allows the function to produce a value that can be used elsewhere in the program.
# Without a return statement, a function returns None by default.
def square(num):
    return num ** 2
result = square(4)
print(f"The square of 4 is: {result}")
