s = input("Enter the string: ")
words = s.split()
long=""
length = 0
for word in words:
    if len(word) > length:
        long=word
        length = len(word)
print(f"The length of the longest word {long} is:",length)
