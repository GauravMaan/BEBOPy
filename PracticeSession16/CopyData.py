def copy_file(source, destination):
    try:
        with open(source, 'r') as src_file:
            content = src_file.read()
        with open(destination, 'w') as dest_file:
            dest_file.write(content)
        print(f"Content copied from {source} to {destination}.")
    except FileNotFoundError:
        print(f"Error: The source file '{source}' does not exist.")
    except PermissionError:
        print("Error: Permission denied while accessing one of the files.")
    except Exception as e:
        print(f"Unexpected error: {e}")
source_file = input("Enter the source file path: ")
destination_file = input("Enter the destination file path: ")
copy_file(source_file, destination_file)