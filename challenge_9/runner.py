from challenge_9 import IntCodeComputer

with open("nine.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line.strip())
program = array[0]

c = IntCodeComputer(program, inputs=[1])
c.run_intcode()
print("".join(str(x) for x in c.outputs))

c = IntCodeComputer(program, inputs=[2])
c.run_intcode()
print("".join(str(x) for x in c.outputs))
