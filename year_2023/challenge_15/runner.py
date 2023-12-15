from year_2023.challenge_15.module import run_hash_algorithm, calculate_focal_lengths

with open("fifteen.txt", "r") as ins:
    init_sequence = []
    for line in ins:
        init_sequence.append(line.strip())
    print(run_hash_algorithm(init_sequence=init_sequence[0]))
    print(calculate_focal_lengths(init_sequence=init_sequence[0]))
