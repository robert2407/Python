def loop(map):
    visited = set()
    result = []

    current_key = 'start'
    while current_key in map and current_key not in visited:
        visited.add(current_key)
        result.append(map[current_key])
        current_key = map[current_key]

        if result.count(map[current_key]) > 1:
            result.pop()
            break

    return result

if __name__ == "__main__":
    mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
    result = loop(mapping)
    print(result)
