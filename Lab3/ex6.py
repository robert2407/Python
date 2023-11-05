def count(input_list):
    unique_set = set()
    duplicates = set()

    for item in input_list:
        if item in unique_set:
            duplicates.add(item)
        else:
            unique_set.add(item)

    return len(unique_set), len(duplicates)

if __name__ == "__main__":
    my_list = [1, 2, 2, 3, 4, 4, 5, 6]
    unique, duplicate = count(my_list)

    print("Number of unique elements:", unique)
    print("Number of duplicate elements:", duplicate)
