from year_2022.challenge_7.module import directory_size, directory_to_delete

with open("seven.txt", "r") as ins:
    commands = []
    for line in ins:
        commands.append(line.strip())
    print(directory_size(commands))
    print(directory_to_delete(commands))
