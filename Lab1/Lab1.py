import math

def cmmdc(numbers):                                   #ex1
    if len(numbers) < 2:
        print("Trebuie sa avem minim 2 nr.")
        return None

    result = numbers[0]
    for num in numbers[1:]:         # pornesc de la elementul cu index 1, adica al doilea
        result = math.gcd(result, num)

    return result


def count(str):                         #ex2
    voc = "AEIOUaeiou"
    voc_count = 0

    for char in str:
        if char in voc:
            voc_count += 1

    return voc_count


def count_occur(main_string, sub_string):         #ex3
    start = 0
    count = 0

    while start < len(main_string):
        start = main_string.find(sub_string, start)
        if start == -1:
            break
        count += 1
        start += 1

    return count


def camel_to_snake(string):                             #ex4
    snake_case = ""
    for char in string:
        if (char.isupper()):
            if (snake_case):
                snake_case += "_"
            snake_case += char.lower()
        else:
            snake_case += char
    return snake_case

def matrix_spiral(matrix):                               #ex5
    result = ""
    while matrix:           #fac asta pana se termina matricea, am facut un "cerc" complet de verificare asa
        # primul rand
        result += "".join(matrix[0])
        matrix = matrix[1:]     # iau elementele in afara de prima linie

        # iau ultimul element din fiecare rand
        for row in matrix:
            result += row[-1]
            row.pop()

        # iau ultimul rand in ordine inversa
        if matrix:
            result += "".join(matrix[-1][::-1])
            matrix.pop()

        # merg pe randuri de jos in sus si iau primul element
        for row in matrix[::-1]:
            result += row[0]
            row.pop(0)

    return result


def palindr(number):                              #ex6
    if number < 0:
        return False

    copy_number = number
    palindrom_check = 0

    while number > 0:
        last_digit = number % 10
        palindrom_check = palindrom_check * 10 + last_digit
        number = number // 10

    return copy_number == palindrom_check

def extract_first_number_only(string):                               #ex7
    found_number = False
    num_str = ""

    for char in string:
        if char.isdigit():
            num_str += char
            found_number = True
        elif found_number:
            break

    if num_str:
        return int(num_str)
    else:
        return None

def count_number_of_bits_1(number):                            #ex8
    repr_bin = bin(number)[2:]  # transofrma direct in binar
    counter = repr_bin.count('1')
    return counter

def most_used_letter(str):                           #ex9
    str = str.lower()  # nu vreau sa fie case sensitive verificarea
    letter_count = {}

    for char in str:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    if not letter_count:
        return None

    most_used_letter_here = None
    max = 0

    for letter, count in letter_count.items():  # verific vect de frcv
        if count > max:
            most_used_letter_here = letter
            max = count

    return most_used_letter_here, max

def count_words(str):                                   #ex10
    num = str.split()  # desfac textul in cuvinte dupa fiecare spatiu
    return len(num)

if __name__ == "__main__":                              #main

    # ex 1
    list_of_numbers = []
    num_count = int(input("Introduceti pentru cate nr verificati: "))

    if num_count < 2:
        print("Trebuie sa avem minim 2 nr.")
    else:
        for i in range(num_count):
            numbr = int(input(f"Numarul: "))
            list_of_numbers.append(numbr)

        cmmdcc = cmmdc(list_of_numbers)

        if cmmdcc is not None:
            print(f"Cmmdc: {cmmdcc}")

    # ex 2
    input_string = input("Un cuvant pentru a calcula numarul de vocale: ")
    vowel_count = count(input_string)

    print(f"Nr de vocale: {vowel_count}")

    # ex 3
    string1 = input("Primul substring: ")
    string2 = input("Stringul in care voi cauta primul string: ")

    count_check = count_occur(string2, string1)
    print(f"Primul string se gaseste in al doilea de: {count_check} ori")

    # ex 4
    input_string = input("UpperCamelCase: ")
    converted_string = camel_to_snake(input_string)
    print(f"lowercase_with_underscores: {converted_string}")

    # ex 5
    matrix = [
        ["f", "i", "r", "s"],
        ["n", "_", "l", "t"],
        ["o", "b", "a", "_"],
        ["h", "t", "y", "p"]
    ]

    res = matrix_spiral(matrix)
    print(res)

    # ex 6
    number = int(input("Vericati ca numarul sa fie palindrom: "))
    if palindr(number):
        print(f"{number} este.")
    else:
        print(f"{number} nu este.")

    # ex 7
    input_text = input("Un text pentru a gasi primul numar din el: ")
    number = extract_first_number_only(input_text)
    if number is not None:
        print(f"Primul numar este: {number}")
    else:
        print("Nu exista numere.")

    # ex 8
    input_number = int(input("Numar pentru a calcula cati biti 1 are: "))       #123123 are 10 de 0 : 11110000011110011
    ones_count = count_number_of_bits_1(input_number)
    print(f"Numarul are {ones_count} biti de 1 in reprezentarea in baza 2.")

    # ex 9
    input_text = input("Text pentru a calcula cea mai utilizata litera: ")
    result = most_used_letter(input_text)
    if result is not None:
        letter, count = result
        print(f"Cea mai utilizata litera este '{letter}', utilizata de {count} ori.")
    else:
        print("Sir vid")

    # ex 10
    input_text = input("Text pentru a calcula numarul de cuvinte ")
    word_counter = count_words(input_text)
    print(f"Numarul de cuvinte din text este: {word_counter}")
