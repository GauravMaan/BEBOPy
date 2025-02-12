# def pairs(lst, target):
#     pairs = []
#     demo = set()
#     for i in lst:
#         j = target - i
#         if j in demo:
#             pairs.append((j, i))
#         demo.add(i)
#
#     return pairs
#
#
# print(pairs([1, 2, 3, 4, 5, 6], 7))



def find_pairs(lst,key):
    n=len(lst)
    ans=[]
    for i in range (n):
        for j in range(i+1,n):
            if lst[i]+lst[j]==key:
                temp=lst[i],lst[j]
                ans.append(temp)
    print(ans)
lst=[1,2,3,4,5,6]
key=7
find_pairs(lst,key)