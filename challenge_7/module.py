from .intcode_computer import IntCodeComputer


def amplifier_chain(intcode_string, phase_sequence_string):
    phase_sequence = [int(x) for x in phase_sequence_string.split(',')]
    amplifier_inputs = [0]
    output = None
    while len(phase_sequence):
        phase_input = phase_sequence.pop(0)
        amplifier_input = amplifier_inputs.pop(0)
        computer = IntCodeComputer(intcode_string, inputs=[phase_input, amplifier_input])
        computer.run_intcode()
        output = computer.outputs[0]
        amplifier_inputs.append(output)
    return output


def _system_halted(amplifiers):
    for computer in amplifiers.values():
        if not computer.is_halted:
            return False
    return True


def repeating_amplifier_chain(intcode_string, phase_sequence_string):
    phase_sequence = [int(x) for x in phase_sequence_string.split(',')]
    amplifiers = {}
    for idx, seq in enumerate(phase_sequence):
        amplifier_input = []
        if idx == 0:
            amplifier_input = [0]
        amplifiers[idx] = IntCodeComputer(intcode_string, inputs=[seq] + amplifier_input)
    last_amp = len(amplifiers) - 1
    while not _system_halted(amplifiers):
        for k, v in amplifiers.items():
            v.run_intcode()
            out = v.outputs[-1]
            if k < last_amp:
                amplifiers[k+1].inputs.append(out)
            else:
                amplifiers[0].inputs.append(out)
    return amplifiers[last_amp].outputs[-1]

