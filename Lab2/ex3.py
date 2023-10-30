# 3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b,
# a reunited with b, a - b, b - a)

def list_operations(a, b):
    intersection = [i for i in a if i in b] # Daca acea valoare i este si in a si in b o pune in intersection
    union = list(a)
    for x in b:
        if x not in union:
            union.append(x)
    a_minus_b = [x for x in a if x not in b]
    b_minus_a = [x for x in b if x not in a]

    return intersection, union, a_minus_b, b_minus_a

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]
    intersection, union, a_minus_b, b_minus_a = list_operations(a, b)

    print("Intersection:", intersection)
    print("Union:", union)
    print("a - b:", a_minus_b)
    print("b - a:", b_minus_a)
