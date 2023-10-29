# 4. Write a function that receives as a parameters a list of musical notes (strings),
# a list of moves (integers) and a start position (integer).
# The function will return the song composed by going though the musical notes beginning with the start position and following the moves given as parameter.
# Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]

def song(notes, moves, start_position):
    song = []
    position = start_position
    song.append(notes[position])

    for i in moves:
        position = (position + i) % len(notes)
        song.append(notes[position])

    return song

if __name__ == "__main__":
    notes = ["do", "re", "mi", "fa", "sol"]
    moves = [1, -3, 4, 2]
    start_position = 2

    result = song(notes, moves, start_position)
    print(result)
