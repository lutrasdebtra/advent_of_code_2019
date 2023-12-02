from typing import List


def sum_possible_game_ids(
    games_list: List[str],
) -> int:
    MAX_CUBES = {"red": 12, "green": 13, "blue": 14}
    id_sum = 0

    for game in games_list:
        game_possible = True
        game_id, game_rounds = game.split(":")
        game_id = int(game_id.split(" ")[-1])
        game_rounds = game_rounds.split(";")
        for game_round in game_rounds:
            cubes = game_round.split(",")
            for cube in cubes:
                cube = cube.strip()
                amount, colour = cube.split(" ")
                if MAX_CUBES[colour] < int(amount):
                    game_possible = False
        if game_possible:
            id_sum += game_id

    return id_sum


def sum_power_of_min_cubes(
    games_list: List[str],
) -> int:
    min_power_sum = 0

    for game in games_list:
        game_id, game_rounds = game.split(":")
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        game_rounds = game_rounds.split(";")
        for game_round in game_rounds:
            cubes = game_round.split(",")
            for cube in cubes:
                cube = cube.strip()
                amount, colour = cube.split(" ")
                if min_cubes[colour] < int(amount):
                    min_cubes[colour] = int(amount)
        min_power_sum += min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
    return min_power_sum
