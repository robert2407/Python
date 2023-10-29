#  8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True.
#  For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True,
#  otherwise it should contain characters that have the ASCII code not divisible by x.

def generate_lists(x=1, strings=None, flag=True):
    if strings is None:
        return []

    result = []
    for str in strings:
        letter_list = []

        for letter in str:
            ascii = ord(letter)

            if (ascii % x == 0 and flag == True) or (ascii % x != 0 and flag == False):
                letter_list.append(letter)      #pt fiecare cuvant pun toate literele

        result.append(letter_list)  #fac o lista pt fiecare string

    return result

if __name__ == "__main__":
    x = 2
    strings = ["test", "hello", "lab002"]
    flag = False

    result = generate_lists(x, strings, flag)
    print(result)
