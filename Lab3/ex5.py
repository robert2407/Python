def validate(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key in dictionary:
            value = dictionary[key]
            if not value.startswith(prefix):
                return False
            if middle not in value[1:-1]:    # incepe de la a doua litera si merge pana la penultima
                return False
            if not value.endswith(suffix):
                return False
        else:
            return False
    return True

if __name__ == "__main__":
    rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    # data = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
    data = {"key1": "come inside, it's too cold out", "key2": "start middle winter"}

    result = validate(rules, data)
    print(result)
