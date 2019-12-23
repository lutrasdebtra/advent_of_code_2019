class IntCodeComputer:
    POSITION_MODE = 'position'
    VALUE_MODE = 'value'
    RELATIVE_MODE = 'relative'

    def __init__(self, intcode_string, inputs=None):
        self.instructions = [int(x) for x in intcode_string.split(',')] + [0 for x in range(1000)]
        self.inputs = inputs if inputs else []
        self.outputs = []
        self.pos = 0
        self.relative_base = 0

        self.is_halted = False

    def _instruction_1(self, modes):
        pos_1, pos_2, pos_3 = \
            self.instructions[self.pos + 1], self.instructions[self.pos + 2], self.instructions[self.pos + 3]
        self.instructions[self._get_output_position(pos_3, modes, 2)] = self._get_instruction(pos_1, modes, 0) + \
                              self._get_instruction(pos_2, modes, 1)
        self.pos += 4

    def _instruction_2(self, modes):
        pos_1, pos_2, pos_3 = \
            self.instructions[self.pos + 1], self.instructions[self.pos + 2], self.instructions[self.pos + 3]
        self.instructions[self._get_output_position(pos_3, modes, 2)] = self._get_instruction(pos_1, modes, 0) * \
                              self._get_instruction(pos_2, modes, 1)
        self.pos += 4

    def _instruction_3(self, modes):
        if len(self.inputs):
            pos_1 = self.instructions[self.pos + 1]
            self.instructions[self._get_output_position(pos_1, modes, 0)] = self.inputs.pop(0)
            self.pos += 2
            return True
        return False

    def _instruction_4(self, modes):
        pos_1 = self.instructions[self.pos + 1]
        self.pos += 2
        self.outputs.append(self._get_instruction(pos_1, modes, 0))
        print(self.outputs)

    def _instruction_5(self, modes):
        pos_1, pos_2 = self.instructions[self.pos + 1], self.instructions[self.pos + 2]
        if self._get_instruction(pos_1, modes, 0) != 0:
            self.pos = self._get_instruction(pos_2, modes, 1)
        else:
            self.pos += 3

    def _instruction_6(self, modes):
        pos_1, pos_2 = self.instructions[self.pos + 1], self.instructions[self.pos + 2]
        if self._get_instruction(pos_1, modes, 0) == 0:
            self.pos = self._get_instruction(pos_2, modes, 1)
        else:
            self.pos += 3

    def _instruction_7(self, modes):
        pos_1, pos_2, pos_3 = \
            self.instructions[self.pos + 1], self.instructions[self.pos + 2], self.instructions[self.pos + 3]
        if self._get_instruction(pos_1, modes, 0) < \
                self._get_instruction(pos_2, modes, 1):
            self.instructions[self._get_output_position(pos_3, modes, 2)] = 1
        else:
            self.instructions[self._get_output_position(pos_3, modes, 2)] = 0
        self.pos += 4

    def _instruction_8(self, modes):
        pos_1, pos_2, pos_3 = \
            self.instructions[self.pos + 1], self.instructions[self.pos + 2], self.instructions[self.pos + 3]
        if self._get_instruction(pos_1, modes, 0) == \
                self._get_instruction(pos_2, modes, 1):
            self.instructions[self._get_output_position(pos_3, modes, 2)] = 1
        else:
            self.instructions[self._get_output_position(pos_3, modes, 2)] = 0
        self.pos += 4

    def _instruction_9(self, modes):
        pos_1 = self.instructions[self.pos + 1]
        self.relative_base += self._get_instruction(pos_1, modes, 0)
        self.pos += 2

    def _get_instruction(self, position, modes, order):
        if order in modes:
            if modes[order] == self.VALUE_MODE:
                return position
            elif modes[order] == self.RELATIVE_MODE:
                return self.instructions[position + self.relative_base]
        return self.instructions[position]

    def _get_output_position(self, position, modes, order):
        if order in modes:
            if modes[order] == self.RELATIVE_MODE:
                return position + self.relative_base
        return position

    def _process_opt_code(self, opt_code):
        opt_code_str = str(opt_code)
        modes = {}
        parameters_, mode_ = opt_code_str[:-2], int(opt_code_str[-2:])
        for i, v in enumerate(reversed(parameters_)):
            if int(v) == 1:
                modes[i] = self.VALUE_MODE
            elif int(v) == 2:
                modes[i] = self.RELATIVE_MODE
            else:
                modes[i] = self.POSITION_MODE
        return mode_, modes

    def run_intcode(self):
        while self.pos < len(self.instructions):
            opt_code, modes = self._process_opt_code(self.instructions[self.pos])
            if opt_code == 99:
                self.is_halted = True
                break
            if opt_code == 1:
                self._instruction_1(modes)
            elif opt_code == 2:
                self._instruction_2(modes)
            elif opt_code == 3:
                result = self._instruction_3(modes)
                if not result:
                    break
            elif opt_code == 4:
                self._instruction_4(modes)
            elif opt_code == 5:
                self._instruction_5(modes)
            elif opt_code == 6:
                self._instruction_6(modes)
            elif opt_code == 7:
                self._instruction_7(modes)
            elif opt_code == 8:
                self._instruction_8(modes)
            elif opt_code == 9:
                self._instruction_9(modes)
