def squares(*args):
    return sum(x**2 for x in args)
n = input("Enter numbers separated by spaces: ").split()
n = [int(num) for num in n]
result = squares(*n)
print(f"Sum of squares of the given numbers: {result}")
