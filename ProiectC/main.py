import os
import filecmp

def remove_duplicates(folder_path):
    duplicates = {}

    for (root, directories, files) in os.walk(folder_path):
        for fileName in files:
            current_path = os.path.join(root, fileName)

            if os.path.isfile(current_path):
                try:
                    with open(current_path, 'r') as file_content:
                        file_content = file_content.read()
                except IOError as e:
                    print(f"Error at reading: {e}")

                if file_content not in duplicates:
                    duplicates[file_content] = [current_path]
                else:
                    for path_duplicate in duplicates[file_content]: #pentru fiecare path verific daca sunt la fel
                        if filecmp.cmp(path_duplicate, current_path):
                            duplicates[file_content].append(current_path)
                            break

    if duplicates:
        duplicate_files = {}
        number_of_duplicates = 1
        has_duplicates  = False

        for duplicate_paths in duplicates.values():
            if len(duplicate_paths) > 1:  # am mai multe fisiere cu continut identic
                print("These ones have the same content:")
                has_duplicates = True
                for current_path in duplicate_paths:    # afisez pathurile duplicate cu acelasi continut
                    print(f"{number_of_duplicates}. {current_path}")
                    duplicate_files[number_of_duplicates] = current_path
                    number_of_duplicates = number_of_duplicates + 1

        delete_duplicates = []
        if not has_duplicates:
            print("The directory has no duplicates ! ")
            return

        while True:
            try:
                keep = input(f"Please select the file you want to keep [1..{number_of_duplicates - 1}] ")
                keep_choices = keep.split(' ')
                keep_choice = []
                for choice in keep_choices:
                    keep_choice.append(int(choice))

                for elems in range(1, number_of_duplicates):    # adaug elementele care trebuie sterse
                    if elems not in keep_choice:                # nu sunt in keep_choice
                        delete_duplicates.append(duplicate_files[elems])

                for delete_path in delete_duplicates:   # sterg elementele
                    if os.path.exists(delete_path):
                        os.remove(delete_path)

                print("Succes ! ")
                break

            except ValueError:
                print("Not valid numbers ! (space between them)")

    else:
        print("The directory has no duplicates ! ")

if __name__ == "__main__":
    folder_path = input("Folder to search in -> ")

    if not os.path.isdir(folder_path):
        print("Folder name does not exist ! ")
    else:
        remove_duplicates(folder_path)