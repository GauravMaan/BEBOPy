def non_repeating(string1):
    tem={}
    for i in string1:
        if i in tem:
            tem[i]+=1
        else:
            tem[i]=1
    for j in string1:
       if tem[j]==1:
            print(j)
            break
string1=input("Enter the String: ")
ans=non_repeating(string1)