from itertools import permutations

from challenge_7 import amplifier_chain, repeating_amplifier_chain


with open("seven.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line.strip())
program = array[0]

max_ = 0
for seq in permutations(range(0, 4 + 1), 5):
    result = amplifier_chain(program, ",".join([str(x) for x in seq]))
    max_ = result if result > max_ else max_
print(max_)

max_ = 0
for seq in permutations(range(5, 9 + 1), 5):
    result = repeating_amplifier_chain(program, ",".join([str(x) for x in seq]))
    max_ = result if result > max_ else max_
print(max_)
