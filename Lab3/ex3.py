def comp(dict1, dict2):
    if set(dict1.keys()) != set(dict2.keys()):      # verific toate cheile sa vad daca sunt la fel, altfel nu mai are rost
        return False                                # sa merg mai departe

    for elem in dict1.keys():
        value1 = dict1[elem]
        value2 = dict2[elem]

        if isinstance(value1, dict) and isinstance(value2, dict):       # daca e dictinoar in dictionar
            if not comp(value1, value2):
                return False

        elif value1 != value2:      #daca nu sunt dictionare
            return False

    return True

if __name__ == "__main__":
    dict1 = {'a': 1, 'b': {'c': 2, 'd': [3, 4]}}
    dict2 = {'a': 1, 'b': {'c': 2, 'd': [3, 4]}}
    dict3 = {'a': 1, 'b': {'c': 2, 'd': [3, 5]}}

    result1 = comp(dict1, dict2)
    result2 = comp(dict1, dict3)

    print("Sunt la fel? dict 1 si dict 2", result1)
    print("Sunt la fel? dict 1 si dict 3", result2)
