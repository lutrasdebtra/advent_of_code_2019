from challenge_5 import run_intcode


with open("five.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line.strip())
program = array[0]

run_intcode(program, input_=1)
run_intcode(program, input_=5)
