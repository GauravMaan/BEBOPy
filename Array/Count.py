my_list = ["hello"]
count = {}

for i in my_list[0]:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)