def pairs(lst, target):
    pairs = []
    demo = set()
    for i in lst:
        j = target - i
        if j in demo:
            pairs.append((j, i))
        demo.add(i)

    return pairs


print(pairs([1, 2, 3, 4, 5, 6], 7))