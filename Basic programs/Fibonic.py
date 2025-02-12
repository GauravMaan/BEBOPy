# n = int(input("enter the number: "))
# a, b = 0, 1
# count = 0
# if n <= 0:
#     print("Please enter a positive integer")
# elif n == 1:
#     print("Fibonacci sequence up to", n, ":")
#     print(a)
# else:
#     # for i in range(n-2):
#     #     c=a+b
#     #     a=b
#     #     b=c
#     #     n=n-2
#     # print(c)
#     print("Fibonacci sequence:")
#     while count < n:
#         print(a, end=" ")
#         tem = a + b
#         a = b
#         b = tem
#         count += 1


def fibonacci(n):
    if n <= 0:
        return []  # Return an empty list for invalid input
    elif n == 1:
        return [0]  # Fibonacci series for n=1 is [0]

    fib_series = [0, 1]  # Initialize the first two terms
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])  # Compute next Fibonacci number

    return fib_series
n = 10
print(fibonacci(n))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def fibonacci_print(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")  # Print each Fibonacci number
        a, b = b, a + b  # Update values
fibonacci_print(10)  # Output: 0 1 1 2 3 5 8 13 21 34
