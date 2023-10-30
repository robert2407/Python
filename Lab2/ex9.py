#9. Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium and
# will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game.
# A spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are occupied.
# All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest row from the field.

def find_seats(matrix):
    occup = []
    rows = len(matrix)
    columns = len(matrix[0])

    for col in range(columns):
        for row in range(rows):
            current = matrix[row][col]

            blocked = False                   # verific pe fiecare rand ca un spectator de mai jos sa nu
            for i in range(row):                 # fie mai mic sau egal decat unul de mai sus
                if matrix[i][col] >= current:
                    blocked = True
                    break

            if blocked:
                occup.append((row, col))

    return occup

if __name__ == "__main__":
    stadium = [
        [1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5]
    ]

    result = find_seats(stadium)
    print(result)
