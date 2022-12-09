from year_2022.challenge_9.module import rope_positions

with open("nine.txt", "r") as ins:
    moves = []
    for line in ins:
        direction, distance = line.strip().split()
        moves.append((direction, int(distance)))
    print(rope_positions(moves, tail_length=1))
    print(rope_positions(moves, tail_length=9))
