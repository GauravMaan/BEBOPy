def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if not content:
                raise ValueError("The file is empty.")
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except UnicodeDecodeError:
        print("Error: Encoding error while reading the file.")
    except Exception as e:
        print(f"Unexpected error: {e}")
file_path = input("Enter the file path: ")
word_count = process_file(file_path)
if word_count is not None:
    print(f"Total number of words in the file: {word_count}")