def my_function(*arguments, **keywords):
    k = 0
    for elem in arguments:
        if elem in keywords.values():
            k += 1
    return k

if __name__ == "__main__":
    result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
    print(result)
