# file=open("/Users/gauravmaan/Desktop/BEBOPy/FileHandling/FileHandling.txt", 'w')
# for i in range(5):
#     file.write("This is first file created by file handling \n")
# file.close()
# print("file ban gyi")


##read the file
# file=open("/Users/gauravmaan/Desktop/BEBOPy/FileHandling/FileHandling.txt", 'r')
# print(file.read())

# file=open("/Users/gauravmaan/Desktop/BEBOPy/FileHandling/FileHandling.txt", 'r')
# print(file.readline())

##appending the file
# file=open("/Users/gauravmaan/Desktop/BEBOPy/FileHandling/FileHandling.txt", 'a')
# file.write("Radha Raman Hari Bol \n")
# file.write("jai jai Radha Raman Hari Bol \n")
# file.close()
# print("Done")
import os
try:
    os.remove("/Users/gauravmaan/Desktop/BEBOPy/FileHandling/FileHandling.txt")
    print("done")
except Exception as e:
    print(e)

