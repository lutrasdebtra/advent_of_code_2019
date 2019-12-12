class IntCodeComputer:

    def __init__(self, intcode_string, inputs=None):
        self.instructions = [int(x) for x in intcode_string.split(',')]
        self.inputs = inputs if inputs else []
        self.outputs = []
        self.pos = 0

    def _instruction_1(self, immediate_modes):
        pos_1, pos_2, pos_3 = \
            self.instructions[self.pos + 1], self.instructions[self.pos + 2], self.instructions[self.pos + 3]
        self.instructions[pos_3] = self._get_instruction(pos_1, value_mode=(0 in immediate_modes)) + \
                              self._get_instruction(pos_2, value_mode=(1 in immediate_modes))
        self.pos += 4

    def _instruction_2(self, immediate_modes):
        pos_1, pos_2, pos_3 = \
            self.instructions[self.pos + 1], self.instructions[self.pos + 2], self.instructions[self.pos + 3]
        self.instructions[pos_3] = self._get_instruction(pos_1, value_mode=(0 in immediate_modes)) * \
                              self._get_instruction(pos_2, value_mode=(1 in immediate_modes))
        self.pos += 4

    def _instruction_3(self, input_):
        if input_:
            pos_1 = self.instructions[self.pos + 1]
            self.instructions[pos_1] = input_
        self.pos += 2

    def _instruction_4(self):
        pos_1 = self.instructions[self.pos + 1]
        self.pos += 2
        self.outputs.append(self.instructions[pos_1])
        print(self.outputs)

    def _instruction_5(self, immediate_modes):
        pos_1, pos_2 = self.instructions[self.pos + 1], self.instructions[self.pos + 2]
        if self._get_instruction(pos_1, value_mode=(0 in immediate_modes)) != 0:
            self.pos = self._get_instruction(pos_2, value_mode=(1 in immediate_modes))
        else:
            self.pos += 3

    def _instruction_6(self, immediate_modes):
        pos_1, pos_2 = self.instructions[self.pos + 1], self.instructions[self.pos + 2]
        if self._get_instruction(pos_1, value_mode=(0 in immediate_modes)) == 0:
            self.pos = self._get_instruction(pos_2, value_mode=(1 in immediate_modes))
        else:
            self.pos += 3

    def _instruction_7(self, immediate_modes):
        pos_1, pos_2, pos_3 = \
            self.instructions[self.pos + 1], self.instructions[self.pos + 2], self.instructions[self.pos + 3]
        if self._get_instruction(pos_1, value_mode=(0 in immediate_modes)) < \
                self._get_instruction(pos_2, value_mode=(1 in immediate_modes)):
            self.instructions[pos_3] = 1
        else:
            self.instructions[pos_3] = 0
        self.pos += 4

    def _instruction_8(self, immediate_modes):
        pos_1, pos_2, pos_3 = \
            self.instructions[self.pos + 1], self.instructions[self.pos + 2], self.instructions[self.pos + 3]
        if self._get_instruction(pos_1, value_mode=(0 in immediate_modes)) == \
                self._get_instruction(pos_2, value_mode=(1 in immediate_modes)):
            self.instructions[pos_3] = 1
        else:
            self.instructions[pos_3] = 0
        self.pos += 4

    def _get_instruction(self, position, value_mode=False):
        if value_mode:
            return position
        return self.instructions[position]

    @staticmethod
    def _process_opt_code(opt_code):
        opt_code_str = str(opt_code)
        immediate_modes = set()
        parameters_, mode_ = opt_code_str[:-2], int(opt_code_str[-2:])

        for i, v in enumerate(reversed(parameters_)):
            if int(v) == 1:
                immediate_modes.add(i)
        return mode_, immediate_modes

    def run_intcode(self):
        while self.pos < len(self.instructions):
            opt_code, immediate_modes = self._process_opt_code(self.instructions[self.pos])
            if opt_code == 99:
                break
            if opt_code == 1:
                self._instruction_1(immediate_modes)
            elif opt_code == 2:
                self._instruction_2(immediate_modes)
            elif opt_code == 3:
                self._instruction_3(self.inputs.pop(0))
            elif opt_code == 4:
                self._instruction_4()
            elif opt_code == 5:
                self._instruction_5(immediate_modes)
            elif opt_code == 6:
                self._instruction_6(immediate_modes)
            elif opt_code == 7:
                self._instruction_7(immediate_modes)
            elif opt_code == 8:
                self._instruction_8(immediate_modes)