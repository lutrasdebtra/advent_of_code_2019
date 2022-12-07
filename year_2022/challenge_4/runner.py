from year_2022.challenge_4.module import get_subseqs, get_overlaps

with open("four.txt", "r") as ins:
    assignments = []
    for line in ins:
        assignments.append(line.strip())
    print(get_subseqs(assignments))
    print(get_overlaps(assignments))
