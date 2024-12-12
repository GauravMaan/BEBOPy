file=open("/PracticeSession13/example.txt", 'w')
file.write("Python programming is interesting")
file.close()
print("Crated")


file=open("/PracticeSession13/example.txt", 'r')
print(file.read())