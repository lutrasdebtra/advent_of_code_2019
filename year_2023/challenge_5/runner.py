from year_2023.challenge_5.module import (
    calculate_lowest_location_seed_numbers,
    calculate_lowest_location_seed_ranges,
)

with open("five.txt", "r") as ins:
    almanac = []
    for line in ins:
        almanac.append(line.strip())
    print(calculate_lowest_location_seed_numbers(almanac=almanac.copy()))
    print(calculate_lowest_location_seed_ranges(almanac=almanac.copy()))
