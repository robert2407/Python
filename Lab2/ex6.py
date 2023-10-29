# 6. Write a function that receives as a parameter a variable number of lists and a whole number x.
# Return a list containing the items that appear exactly x times in the incoming lists.

def finder(x, *lists):
    list_complete = []              # punem toate elem intr-o singura lista
    for i in lists:
        list_complete.extend(i)

    item_counts = {}                # fac un dictionat pt a stoca nr de prezente al cuv.
    for i in list_complete:
        if i in item_counts:
            item_counts[i] += 1
        else:
            item_counts[i] = 1

    result = []
    for i, count in item_counts.items():             # gasesc elem. care apar de x ori
        if count == x:
            result.append(i)

    return result

if __name__ == "__main__":
    list1 = [2, 4, 5, 77, 865, 45]
    list2 = [121, 23432, 25654, 45, 77, 45, "Test"]
    list3 = [34, 212, 45, 214, 5, 45, "Test"]
    x = 2

    result = finder(x, list1, list2, list3)
    print(result)