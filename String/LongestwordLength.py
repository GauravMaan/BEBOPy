# s = input("Enter the string: ")
# words = s.split()
# long=""
# length = 0
# for word in words:
#     if len(word) > length:
#         long=word
#         length = len(word)
# print(f"The length of the longest word {long} is:",length)
#

def find_longest_word(s):
    words = s.split()
    longest_word = ""
    length = 0

    for word in words:
        if len(word) > length:
            longest_word = word
            length = len(word)

    return longest_word, length

s = input("Enter the string: ")
longest_word, length = find_longest_word(s)
print(f"The length of the longest word '{longest_word}' is: {length}")