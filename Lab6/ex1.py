import os
import sys

def read_files_in_directory(directory, extension):
    found = False
    try:
        # daca exista directorul
        if not os.path.isdir(directory):
            raise FileNotFoundError("Invalid directory path")

        # intram in fisierele folderului
        for filename in os.listdir(directory):
            if filename.endswith(extension):
                found = True
                file_path = os.path.join(directory, filename)
                try:
                    # deschidem fisierul si citim din el
                    with open(file_path, 'r') as file:
                        content = file.read()
                        print(f"Contents of {filename}:")
                        print(content)
                        print('+++++++++++++++++++++++++++++++')
                except OSError as e:
                    print(f"Error accessing file {filename}: {e}")
        if not found:
            print(f"No {extension} files found in {directory}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Utilizeaza doua argumente!")
    else:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]
        read_files_in_directory(directory_path, file_extension)
