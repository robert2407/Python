import os
import sys

def calculate_total_file_size(directory):
    size = 0
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError("Invalid path")
        for dirpath, _, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                try:
                    size = os.path.getsize(file_path)
                    size += size
                except OSError as e:
                    print(f"Error accessing file {file_path}: {e}")

        print(f"Size for '{directory}': {size} bytes")

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
        calculate_total_file_size(directory_path)
