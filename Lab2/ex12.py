# 12. Write a function that will receive a list of words  as parameter and will return a list of lists of words,
# grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.

def ryhme(x):
    result_list = [[x[0]]]  # o listsa care contine o lista in care il pun pe x[0]

    for i in range(1, len(x)):
        last_char = x[i][-2:]                 #ult 2 litere
        found = 0

        for word_curr in result_list:
            if word_curr[0][-2:] == last_char: #daca exista ult 2 litere la o lista deja, pune acolo cuvantul
                word_curr.append(x[i])
                found = 1

        if found == 0:
            result_list.append([x[i]])  #adauga o lista noua pt rima actuala
    print(result_list)

if __name__ == "__main__":
    x = ['ana', 'banana', 'carte', 'arme', "parte"]
    ryhme(x)
