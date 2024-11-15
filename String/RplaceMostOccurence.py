s = input("Enter the string: ")
s1=input("Enter the word for replace: ")
s2=input("Ether the word by which it replace: ")
s3 = ""
for i in s:
    if i == s1:
        s3 += s2
    else:
        s3 += i
print(s3)