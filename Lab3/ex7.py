def operat(*sets):
    res = {}

    for i in range(len(sets) - 1):
        for j in range(i + 1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]

            union_result = set1 | set2
            intersection_result = set1.intersection(set2)
            difference1_result = set1 - set2
            difference2_result = set2 - set1

            key_union = f"{set1} sau {set2}"
            key_intersection = f"{set1} si {set2}"
            key_difference1 = f"{set1} Minus {set2}"
            key_difference2 = f"{set2} Minus {set1}"

            res[key_union] = union_result
            res[key_intersection] = intersection_result
            res[key_difference1] = difference1_result
            res[key_difference2] = difference2_result

    return res

if __name__ == "__main__":
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}

    result = operat(set1, set2)

    for key, value in result.items():
        print(f"{key}: {value}")