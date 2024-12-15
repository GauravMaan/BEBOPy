class DivisionByZeroError(Exception):
    pass

def safe_divide(a, b):
    if b == 0:
        raise DivisionByZeroError("Error: Cannot divide by zero.")
    return a / b
try:
    result = safe_divide(10, 0)
    print(f"Result: {result}")
except DivisionByZeroError as e:
    print(e)