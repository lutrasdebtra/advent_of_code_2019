from typing import List


class Module:
    LOW_PULSE = 0
    HIGH_PULSE = 1
    registry = {}
    pulse_counter = {0: 0, 1: 0}
    button_press_counter = 0
    lowest_to_rx = None

    pulse_queue = []

    def __init__(self, name: str, destination_modules: List[str]):
        self.name = name
        self.destination_modules = destination_modules
        self.registry[self.name] = self

    def _send_pulses(self, pulse: int):
        for name in self.destination_modules:
            self.pulse_counter[pulse] += 1
            self.pulse_queue.append((name, pulse, self.name))

    @classmethod
    def press_button(cls, debug: bool = False):
        cls.pulse_counter[cls.LOW_PULSE] += 1
        cls.button_press_counter += 1
        if debug:
            print(f"button -{'low'}-> broadcaster")
        cls.registry["broadcaster"].run(pulse=cls.LOW_PULSE)

        while cls.pulse_queue:
            name, pulse, connected_input = cls.pulse_queue.pop(0)
            if debug:
                print(f"{connected_input} -{'high' if pulse else 'low'}-> {name}")
            try:
                if name == "rx" and pulse == cls.LOW_PULSE:
                    cls.lowest_to_rx = cls.button_press_counter
                cls.registry[name].run(pulse=pulse, connected_input=connected_input)
            except KeyError:
                continue

    @classmethod
    def calculate_pulse_value(cls) -> int:
        return cls.pulse_counter[cls.LOW_PULSE] * cls.pulse_counter[cls.HIGH_PULSE]


class Broadcast(Module):
    def run(self, pulse: int):
        self._send_pulses(pulse=pulse)


class FlipFlop(Module):
    def __init__(self, name: str, destination_modules: List[str]):
        super().__init__(name=name, destination_modules=destination_modules)
        self.on = False

    def run(self, pulse: int, **kwargs):
        if pulse == 1:
            return
        if self.on:
            self.on = False
            pulse_to_send = self.LOW_PULSE
        else:
            self.on = True
            pulse_to_send = self.HIGH_PULSE
        self._send_pulses(pulse=pulse_to_send)


class Conjunction(Module):
    def __init__(
        self, name: str, destination_modules: List[str], connected_inputs: List[str]
    ):
        super().__init__(name=name, destination_modules=destination_modules)
        self.remembered_pulses = {c: self.LOW_PULSE for c in connected_inputs}

    def run(self, pulse: int, connected_input: str):
        self.remembered_pulses[connected_input] = pulse

        if set(self.remembered_pulses.values()) == {self.HIGH_PULSE}:
            pulse_to_send = self.LOW_PULSE
        else:
            pulse_to_send = self.HIGH_PULSE
        self._send_pulses(pulse=pulse_to_send)


def _process_input(modules: List[str]) -> Broadcast:
    module_dict = {}

    for line in modules:
        module, destination_modules = line.split(" -> ")
        destination_modules = [d.strip() for d in destination_modules.split(",")]
        if not module == "broadcaster":
            module_type = module[0]
            module_name = module[1:]
        else:
            module_type = module
            module_name = module
        module_dict[module_name] = {
            "type": module_type,
            "destination_modules": destination_modules,
            "connected_inputs": [],
        }

    # Add connected inputs for Conjunction Modules.
    for name, v in module_dict.items():
        for destination in v["destination_modules"]:
            try:
                module_dict[destination]["connected_inputs"].append(name)
            except KeyError:
                continue

    broadcast = None
    for name, v in module_dict.items():
        module_type = v["type"]
        if module_type == "broadcaster":
            broadcast = Broadcast(
                name=name, destination_modules=v["destination_modules"]
            )
        elif module_type == "%":
            FlipFlop(name=name, destination_modules=v["destination_modules"])
        elif module_type == "&":
            Conjunction(
                name=name,
                destination_modules=v["destination_modules"],
                connected_inputs=v["connected_inputs"],
            )
    return broadcast


def calculate_pulses(modules: List[str]) -> int:
    broadcast = _process_input(modules=modules)
    for _ in range(1000):
        broadcast.press_button()

    return broadcast.calculate_pulse_value()


def calculate_presses_to_rx(modules: List[str]) -> int:
    broadcast = _process_input(modules=modules)
    i = 0
    while not broadcast.lowest_to_rx:
        i += 1
        if i % 1000 == 0:
            print(i)
        broadcast.press_button()

    return broadcast.lowest_to_rx
