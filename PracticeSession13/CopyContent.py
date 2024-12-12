def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        with open(destination_file, 'w') as dest:
            dest.write(content)
        print("done")
    except FileNotFoundError:
        print(f"The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
source_file = "/Users/gauravmaan/Desktop/BEBOPy/PracticeSession13/source.txt"
destination_file = "/Users/gauravmaan/Desktop/BEBOPy/PracticeSession13/destination.txt"
copy_file(source_file, destination_file)