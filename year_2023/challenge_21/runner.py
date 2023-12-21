from year_2023.challenge_21.module import calculate_reachable_plots

with open("twentyone.txt", "r") as ins:
    garden_plots = []
    for line in ins:
        garden_plots.append(line.strip())
    print(calculate_reachable_plots(garden_plots=garden_plots, cutoff=64))
