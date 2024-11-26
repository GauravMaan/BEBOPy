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
def my_arguments2(i,j=200): # Default argument
    print(i,j)
my_arguments2(i=10,j=20)
my_arguments2(i=10)

def my_arguments3(i,j,a):
    print(i,j,a)
my_arguments3(10,20,a=30)
