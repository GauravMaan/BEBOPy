# the variable create outside the function are called as global variable
# the variable create inside the function are called as local variable,cannot accessed outside the function

# global_var=100
# def my_var():
#     local_var=10
#     print(local_var)
# print(global_var)
# my_var()

# #local and global has same name
# xy=200
# def my_var1():
#     xy=100
#     print(xy)
# my_var1()
# print(xy)

#change the global var inside the function using global keyword
# xy=100
# def my_var2():
#     global xy #global keyword
#     xy=200
#     print(xy)
# my_var2()
# print(xy)

xy=100
def my_var3():
    global xy
    xy=200
    print(xy)
# my_var3()
print(xy)

