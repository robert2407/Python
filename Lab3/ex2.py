def counter(text):
    dictionar = {}
    for char in text:
        dictionar[char] = dictionar.get(char, 0) + 1        # pun 0 daca nu este nimic in dict, altfel adaug 1 pt acea litera
    return dictionar

if __name__ == "__main__":
    input_string = "Robert este un om."
    test = counter(input_string)
    print(test)
