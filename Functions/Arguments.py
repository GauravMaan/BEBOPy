#Fixed Argument
# # Positional arguments
# def my_arguments(i,j):
#     print(i,j)
# my_arguments(10,20) #positional argument
#
# # Keyword argument
# def my_arguments1(j,i):
#     print(j,i)
# my_arguments1(i=72727,j=81818) #keyword argument
#
# # Default argument
# def my_arguments2(i,j=200): # Default argument
#     print(i,j)
# my_arguments2(i=10,j=20)
# my_arguments2(i=10)
#
# def my_arguments3(i,j,a):
#     print(i,j,a)
# my_arguments3(10,20,a=30)

#Variable Argument
## *args= positional variable length arg
## **kwargs= keyword variable length arg,pass as key value pair (dict)
## passed as tuple to the function
## allow the args to accept any no of positional args

# def my_first(*name): # *args
#     print("hello",{name})
# my_first("dived")
# my_first("gaurav","vivek")

# def student(**kwargs):
#     for key,value in kwargs.items():
#         print(f'{key} {value}')
# student(name="bob",id="1010")

def display(*args,**kwargs):
    print(args)
    print(kwargs)
display(1,2,3,4,name="gaurav",sal=40000)

#*args with Positional
def greet(name,*args):
    print(name,args)
greet("gaurav","vivek","bob",1,2,3,4)


def greet(name,*args,**kwagrs):
    print(name)
    for i in args:
        print(i)
    for i,j in kwagrs.items():
        print(f"{i} {j}")
greet("gaurav","vivek","bob",1,2,3,4,name1="noob")