import os


def rename_files(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError("Invalid directory path")

        files = os.listdir(directory)
        files.sort()  # sortam fisierele dupa nume

        for index, filename in enumerate(files, start=1):
            old_file_path = os.path.join(directory, filename) # luam calea fisierului
            new_file_name = f"file{index}{os.path.splitext(filename)[1]}" # putem file1.txt, file2.txt etc
            new_file_path = os.path.join(directory, new_file_name)         # daca exista deja, e eroare

            try:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed {filename} to {new_file_name}") # putem sa modificam
            except OSError as e:
                print(f"Error renaming {filename}: {e}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    rename_files(directory_path)
