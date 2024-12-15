try:
    with open('data.txt', 'r') as file:
        content = file.read()
        if not content:
            raise ValueError("The file is empty.")
        print(content)
except FileNotFoundError:
    print("Error: The file 'data.txt' does not exist.")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Unexpected error: {e}")