from year_2022.challenge_7.module import directory_size

with open("seven.txt", "r") as ins:
    commands = []
    for line in ins:
        commands.append(line.strip())
    print(directory_size(commands))
