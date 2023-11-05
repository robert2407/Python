def lit_of_sets(a, b):
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    a_minus_b = list(set(a) - set(b))
    b_minus_a = list(set(b) - set(a))

    return intersection, union, a_minus_b, b_minus_a

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]
    intersection, union, a_minus_b, b_minus_a = lit_of_sets(a, b)

    print("Intersection:", intersection)
    print("Union:", union)
    print("a - b:", a_minus_b)
    print("b - a:", b_minus_a)