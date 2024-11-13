#string is immutable.

# s="Gaurav"
# s[0]="V"
# print(s) #TypeError: 'str' object does not support item assignment

# b='Gaurav'
# print(id(b))

# c=str("gaurav")
# print(c)

# d=str('gaurav')
# print(d)

# n=''
# n=""
# s=str()

# a="gaurav "
# b="maan"
# c=a+b
# print(c)
# print(a*10)

# str="welcome"
# print(str[1:6])
# print(str[:-6])
# print(str[-4:-1])
# print(str[:-2])
#
# print(ord("V"))
# print(ord("g"))
#
# print(ord("A"))
# print(chr(65))

# print(max("Gv"))

# print(len("Gaurav"))

# s="welcome"
# print("come" in s)
# print("come" not in s)
# print("cme" in s)
# print("cme" not in s)

# print("maan">"Maan")
# print("teeth"=="teeth")
# print("abc">" ")
# print("panner"<"milk")
# print("panner"!="milk")

# print('welcome'.isalnum())
# print('welcome123'.isalnum())
# print('123'.isalnum())
#
# s="gaurav maan"
# print(s.isalpha())
# s="gauravmaan"
# print(s.isalpha())
# s="gauravmaan123"
# print(s.isalpha())
#
# s='123433'
# print(s.isdigit())

# s="gauravmaan"
# print(s.islower())
# s="gauravmaan123"
# print(s.isupper())

# s="gaurav maan"
# print(s.isspace())
# s=" "
# print(s.isspace())

# s="gaurav maan"
# print(s.endswith("aan"))
# s="gaurav maan"
# print(s.startswith("gau"))

# s="gaurav maan"
# print(s.find("u"))
# s="gaurav maan"
# print(s.find("w"))

# s="gaurav maan"
# print(s.count("a"))


print("Converting the string")

print("gaurav".capitalize())
print("gaurav".title())
print("gaurav".lower())
print("gaurav".swapcase())
print("GAURAV".swapcase())
print("gaurav".replace("ga","ve"))