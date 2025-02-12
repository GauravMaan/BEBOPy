# # check enter no is prime no or not
# N = int(input("Enter the number:"))
# prime = True
# if N <= 1:
#     prime = False
# else:
#     for i in range(2, int(N/2) + 1):
#         if N % i == 0:
#             prime = False
#             break
# if prime:
#     print("It's a prime number.")
# else:
#     print("Not a prime number.")




def is_prime(n):
    if n < 2:
        return False  # Prime numbers are greater than 1
    for i in range(2, n):  # Check divisibility from 2 to n-1
        if n % i == 0:
            return False  # If divisible, it's not prime
    return True  # If no divisors found, it's prime


print(is_prime(3))  # Output: True
print(is_prime(10)) # Output: False