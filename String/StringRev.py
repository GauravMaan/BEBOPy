s="welcome bro"
s2=" "
for i in s:
    s2=i+s2
print(s2)

s="vivek noob"
s2=s[::-1]
print(s2)

s1="gaurav pro"
a=s1.split()
empty=[]
for i in a:
    s2=""
    for j in i:
        s2=j+s2
    empty.append(s2)
result=" ".join(empty)
print(result)