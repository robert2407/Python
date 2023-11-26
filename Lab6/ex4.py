import os
import sys
from collections import defaultdict

def count_files_by_extension(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError("Invalid path")

        file_extensions = defaultdict(int) # dictionar cu valori default 0

        files = os.listdir(directory)
        if not files:
            print("Directory is empty")
            return

        for file_name in files:
            if os.path.isfile(os.path.join(directory, file_name)): # daca e fisier
                extension = os.path.splitext(file_name)[1] # luam extensia
                file_extensions[extension] += 1

        if not file_extensions:
            print("No files with extensions found in the directory")
        else:
            print("File counts by extension:")
            for ext, count in file_extensions.items(): # parcurg dictionarul
                print(f"{ext}: {count}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Da doar un parametru - calea directorului")
    else:
        directory_path = sys.argv[1]
        count_files_by_extension(directory_path)
