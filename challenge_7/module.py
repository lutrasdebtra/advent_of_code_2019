from .intcode_computer import IntCodeComputer

def amplifier_chain(intcode_string, phase_sequence_string):
    phase_sequence = [int(x) for x in phase_sequence_string.split(',')]
    amplifier_inputs = [0]
    output = None
    while len(phase_sequence):
        phase_input = phase_sequence.pop(0)
        amplifier_input = amplifier_inputs.pop(0)
        computer = IntCodeComputer(intcode_string, inputs=[amplifier_input, phase_input])
        computer.run_intcode()
        output = computer.outputs[0]
        amplifier_inputs.append(output)
    return output
