# def palindrome(string1):
#     srg = ""
#     for i in string1:
#         srg = i + srg
#     return srg

# string1 = input("Enter the String: ")
# reversed_string = palindrome(string1)
# if string1.lower() == reversed_string.lower():
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# def frequency(string1):
#     strg={}
#     for i in string1:
#         if i in strg:
#             strg[i]+=1
#         else:
#             strg[i]=1
#     return strg

# string1=input("Enter the string: ")
# ans=frequency(string1)
# print(ans)

# def non_repeating(string1):
#     tem={}
#     for i in string1:
#         if i in tem:
#             tem[i]+=1
#         else:
#             tem[i]=1
#     for j in string1:
#       if tem[j]==1:
#             print(j)
#             break
# string1="ggaurav"
# ans=non_repeating(string1)

# def anagrams(str1, str2):
#     return sorted(str1) == sorted(str2)
# string1 = "ggaurav"
# string2 = "auravgg"
# if anagrams(string1, string2):
#     print("Anagrams")
# else:
#     print("Not Anagrams")


# def substring(s):
#     current = ""
#     longest = ""
#     for char in s:
#         if char in current:
#             current = current[current.index(char) + 1:]
#         current += char
#         if len(current) > len(longest):
#             longest = current
#     return len(longest), longest

# string1 = "is vivek"
# length, longest_substring = substring(string1)
# print("Length:", length)
# print("Substring:", longest_substring)

# def rever(s1):
#     a=s1.split()
#     empty=[]
#     for i in a:
#         s2=""
#         for j in i:
#             s2=j+s2
#         empty.append(s2)
#     result=" ".join(empty)
#     print(result)

# s1="gaurav pro"
# rever(s1)

# def count_vowels(s):
#     vow = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vow:
#             count += 1

#     return count

# string1 = "Gaurav Pro"
# print(count_vowels(string1))

# def word(s):
#     words = s.split()
#     longest_word = ""
#     length = 0

#     for word in words:
#         if len(word) > length:
#             longest_word = word
#             length = len(word)

#     return longest_word, length

# s = input("Enter the string: ")
# longest_word, length = word(s)
# print(f"The length of the longest word '{longest_word}' is: {length}")

# s = input("Enter the string: ")
# s1 = {}
# for i in s:
#     if i in s1:
#         s1[i] += 1
#     else:
#         s1[i] = 1
# print(s1)


# s="thid id id did did "
# a=s.split()
# s1=[]
# for i in a:
#     if i not in s1:
#         s1.append(i)
# result=" ".join(s1)
# print(result)

# def compress_string(s):
#     if not s:
#         return ""
#     s2 = ""
#     count = 1
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             s2 += s[i - 1] + str(count)
#             count = 1
#     s2 += s[-1] + str(count)
#     return s2
# s = input("Enter the string to compress: ")
# print(compress_string(s))