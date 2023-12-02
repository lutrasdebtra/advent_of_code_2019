from year_2023.challenge_2.module import sum_possible_game_ids, sum_power_of_min_cubes

with open("two.txt", "r") as ins:
    games_list = []
    for line in ins:
        games_list.append(line.strip())
    print(sum_possible_game_ids(games_list=games_list))
    print(sum_power_of_min_cubes(games_list=games_list))
