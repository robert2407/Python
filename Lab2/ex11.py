# Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.
# Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def sort(tupl):
    for i in range(len(tupl) -  1):
        for j in range(i + 1, len(tupl)):
            if tupl[i][1][2] > tupl[j][1][2]:       #al treilea caracter al ceilui de-al doilea element din fiecare tupla
                temp = tupl[i]
                tupl[i] = tupl[j]
                tupl[j] = temp
    return tupl

if __name__ == "__main__":
    result = sort([('abc', 'bcd'), ('abc', 'zza')])
    print(result)
