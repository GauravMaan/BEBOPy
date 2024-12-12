from datetime import datetime
file_path = "/Users/gauravmaan/Desktop/BEBOPy/PracticeSession13/log.txt"
with open(file_path, 'a') as file:
    current_date = datetime.now()
    file.write(current_date.strftime("%Y-%m-%d %H:%M:%S") + '\n')
print(current_date)