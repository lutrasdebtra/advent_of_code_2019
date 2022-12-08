from year_2022.challenge_8.module import visible_trees, scenic_score

with open("eight.txt", "r") as ins:
    adjacency_matrix = []
    for line in ins:
        adjacency_matrix.append([int(x) for x in line.strip()])
    print(visible_trees(adjacency_matrix))
    print(scenic_score(adjacency_matrix))
