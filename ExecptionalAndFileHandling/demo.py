
# print("Yooo")
# try:
#     print(10/0)
#     print(10/5)
#     print(10/0)
# except:
#    print("wrong code")
# except Exception as a:
#     print(a)
#
# n=10
# n1=0
# try:
#     ans=n-n1
#     print(ans)
# except Exception as a:
#     print(a)
# else:
#     print("koi exception nhi hai")
# finally:
#     print("chal gya code")

# def yoo():
#     raise ValueError("An error occurred.")
# try:
#     age = int(input("Enter age: "))
#     if age % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")
#     yoo()
class NegativeValueError(Exception):
    pass

def check_value(value):
    if value < 0:
        raise NegativeValueError("Badmashi ni mitar!")

try:
    check_value(-10)
except NegativeValueError as e:
    print(e)

