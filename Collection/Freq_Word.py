def freq(list1):
    dic={}
    for i in list1:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return dic
list1=["hello python is language"]
words_list = list1[0].split()
print(freq(words_list))