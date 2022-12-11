from year_2022.challenge_11.module import find_active_monkeys

with open("eleven.txt", "r") as ins:
    monkey_inputs = []
    for line in ins:
        monkey_inputs.append(line)
    print(find_active_monkeys(monkey_inputs, 20))
    print(find_active_monkeys(monkey_inputs, 10000, worry_level_decrease=False))
