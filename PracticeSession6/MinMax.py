def max_min(num):
    maxi = num[0]
    mini = num[0]
    for i in num:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i
    return maxi, mini
my_list=[1,2,3,4,5]
print(max_min(my_list))