def write_to_file():
    try:
        filename = input("Enter the filename to write to: ").strip()
        if not filename:
            raise ValueError("Invalid filename. Filename cannot be blank.")
        data = input("Enter the data you want to write to the file: ")
        with open(filename, 'w') as file:
            file.write(data)
            print(f"Data has been written to {filename}.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except PermissionError:
        print("Error: Permission denied when trying to write to the file.")
    except Exception as e:
        print(f"Unexpected error: {e}")
write_to_file()