def most_frequent_character(string):
    frequency = {}
    for i in string:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    max_char = None
    max_count = 0

    for i in frequency:
        if frequency[i] > max_count:
            max_count = frequency[i]
            max_char = i

    return max_char, max_count
string = "hello world"
char, count = most_frequent_character(string)
print(f"Most Frequent Character: '{char}' (Appears {count} times)")