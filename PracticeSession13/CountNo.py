def count(file_path="/Users/gauravmaan/Desktop/BEBOPy/PracticeSession13/document.txt"):
    count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                count += len(line.split())
        return count
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return 0
file_path = "/Users/gauravmaan/Desktop/BEBOPy/PracticeSession13/document.txt"
total_words = count(file_path)
print(f"Total number of words: {total_words}")