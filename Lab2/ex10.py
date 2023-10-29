# 10. Write a function that receives a variable number of lists and returns a list of tuples as follows:
# the first tuple contains the first items in the lists, the second element contains the items on the position 2
# in the lists, etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")].

def touple_maker(*lists):  #zip?            #returneaza o pereche de tuple
    maxi_lenght = 0
    for i in lists:
        if maxi_lenght < len(i):
            maxi_lenght = len(i)
    result = []

    for i in range(maxi_lenght):
        tupl = ()
        for element in lists:
            if i < len(element):
                tupl += (element[i],)       # daca toate au un "coleg"
            else:
                tupl += (None,)             # daca una ramane singura in tupla
        result.append(tupl)

    return result

if __name__ == "__main__":
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7, 8, 9]
    list3 = ["a", "b", "c"]

    result = touple_maker(list1, list2, list3)
    print(result)
