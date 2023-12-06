from year_2023.challenge_6.module import calculate_total_ways_to_beat_races

with open("six.txt", "r") as ins:
    races = []
    for line in ins:
        races.append(line.strip())
    print(calculate_total_ways_to_beat_races(races=races.copy(), join_races=False))
    print(calculate_total_ways_to_beat_races(races=races.copy(), join_races=True))
