try:
    with open('records.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line, end='')
except FileNotFoundError:
    print("Error: The file 'records.txt' does not exist.")
except PermissionError:
    print("Error: You do not have permission to read 'records.txt'.")
except Exception as e:
    print(f"Unexpected error: {e}")