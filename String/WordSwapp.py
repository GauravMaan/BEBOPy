# s = "i am python"
# s2 = " ".join(word[::-1]
# for word in s.split())
# print(s2)

# s = "i am python"
# s2 = ""
# for word in s.split():
#     rev = ""
#     for char in word:
#         rev = char + rev
#     s2 += rev + " "
#
# s2 = s2.strip()
# print(s2)

s="i am don"
s2=s.split()
for i in s2:
    r=s2[-1: : -1]
    print(r)