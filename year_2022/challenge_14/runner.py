from year_2022.challenge_14.module import sand_counter

with open("fourteen.txt", "r") as ins:
    rock_coords = []
    for line in ins:
        rock_coords.append(line.strip())
    print(sand_counter(rock_coords))
    print(sand_counter(rock_coords, add_floor=True))
