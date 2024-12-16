# n=5
# for i in range(n+1):
#     if i%2==0:
#         print(i)
# n=5
# i=1
# while i<n:
#     if i%2==0:
#         print(i)
#     i+=1

# list1=[1,2,3,4,5]
# for i in list1:
#     print(i)
# n=10
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# n=5
# first=0
# second=1
# for i in range(n):
#     print(first)
#     tem=first+second
#     first=second
#     second=tem
#     first,second=second,first+second

# string1="gaurav"
# if string1==string1[::-1]:
#     print("palindrom")
# else:
#     print("not")
# n=121
# tem=n
# reverse=0
# while tem>0:
#     rem=tem%10
#     reverse=(reverse*10)+rem
#     tem=tem//10
# print(reverse)
# if n==reverse:
#     print("yes")
# else:
#     print("no")

# s="thid id id did did "
# a=s.split()
# s1=[]
# for i in a:
#     if i not in s1:
#         s1.append(i)
# result=" ".join(s1)
# print(result)

# s1="gauRav maan"
# a=s1.split()
# s2=[]
# for i in a:
#     s2.append(i[0].lower()+i[1:].upper())
# res=" ".join(s2)
# print(res)

# str1="gaurav maan a nana n nan a na"
# a=str1.split()
# ans=[]
# for i in a:
#     space=""
#     for j in range(len(i)):
#         if j==0:
#             space+=i[j].upper()
#         else:
#             space+=i[j].lower()
#     ans.append(space)
# result=" ".join(ans)
# print(result)

# s1="gaurav saurav maan"
# a=s1.split()
# ans=""
# count=0
# for i in a:
#     if len(i)>count:
#         ans=i
#         count=len(i)
# print(f"{ans} {count}")
#
# s1 = "gaurav saurav maan"
# a = s1.split()
# ans = ""
# count = 0
# for i in a:
#     temp = 0
#     for _ in i:
#         temp += 1
#     if temp > count:
#         ans = i
#         count = temp
#
# print(f"{ans} {count}")

# str1="gggggagaggaggaga"
# count=0
# for i in str1:
#     count+=1
# print(count)

# s1="gaurav pro"
# s2=""
# for i in s1:
#     s2=i+s2
# print(s2)

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