from year_2023.challenge_17.module import calculate_shortest_distance

with open("seventeen.txt", "r") as ins:
    city_blocks = []
    for line in ins:
        city_blocks.append(line.strip())
    print(calculate_shortest_distance(city_blocks=city_blocks, ultra=False))
    print(calculate_shortest_distance(city_blocks=city_blocks, ultra=True))
