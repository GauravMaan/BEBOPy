def string_to_words(string):
    words = []
    word = ""
    for i in string + " ":
        if i != " ":
            word += i
        else:
            if word:
                words.append(word)
            word = ""
    return words
string = "Hello, how are you?"
word_list = string_to_words(string)
print("List of words:", word_list)