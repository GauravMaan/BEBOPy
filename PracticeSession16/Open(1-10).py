def write_numbers_to_file():
    try:
        with open('numbers.txt', 'w') as file:
            numbers = list(range(1, 11))
            for number in numbers:
                file.write(f"{number}\n")
    finally:
        print("File has been closed.")
write_numbers_to_file()