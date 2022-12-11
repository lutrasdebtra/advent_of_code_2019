from typing import List, Text, Optional
import re


class Monkey:
    monkeys: List["Monkey"] = []

    @staticmethod
    def _monkey_input_list(monkey_inputs: List[Text]) -> List[List[Text]]:
        return [monkey_inputs[i : i + 7] for i in range(0, len(monkey_inputs), 7)]

    @staticmethod
    def bulk_create(monkey_inputs: List[Text]):
        for monkey_input in Monkey._monkey_input_list(monkey_inputs):
            Monkey(monkey_input)

    def __init__(self, monkey_input: List[Text]):
        self.items: List[int] = [
            int(m.group(0)) for m in re.finditer(r"(\d+)", monkey_input[1].strip())
        ]
        self.operation = re.match(
            r"Operation: new = (.+)", monkey_input[2].strip()
        ).group(1)
        self.divisible_by: int = int(
            re.match(r"Test: divisible by (\d+)", monkey_input[3].strip()).group(1)
        )
        self.divisible_by_true_monkey: int = int(
            re.match(r"If true: throw to monkey (\d+)", monkey_input[4].strip()).group(
                1
            )
        )
        self.divisible_by_false_monkey: int = int(
            re.match(r"If false: throw to monkey (\d+)", monkey_input[5].strip()).group(
                1
            )
        )

        self.inspection_count = 0

        self.monkeys.append(self)

    def inspect_items(
        self, modulo_number: int, worry_level_decrease: Optional[bool] = True
    ):
        for old in self.items.copy():
            self.inspection_count += 1
            old = eval(self.operation)
            if worry_level_decrease:
                old //= 3
            else:
                old %= modulo_number
            if old % self.divisible_by == 0:
                self.monkeys[self.divisible_by_true_monkey].items.append(old)
            else:
                self.monkeys[self.divisible_by_false_monkey].items.append(old)
        self.items = []

    @classmethod
    def run_round(cls, modulo_number: int, worry_level_decrease: Optional[bool] = True):
        for monkey in cls.monkeys:
            monkey.inspect_items(modulo_number, worry_level_decrease)

    @classmethod
    def run_rounds(cls, rounds: int, worry_level_decrease: Optional[bool] = True):
        modulo_number = 1
        for i in [m.divisible_by for m in cls.monkeys]:
            modulo_number *= i
        for _ in range(rounds):
            cls.run_round(modulo_number, worry_level_decrease)

    @classmethod
    def most_active_monkeys(cls) -> int:
        inspection_counts = [monkey.inspection_count for monkey in cls.monkeys]
        inspection_counts.sort(reverse=True)
        return inspection_counts[0] * inspection_counts[1]


def find_active_monkeys(
    monkey_inputs: List[Text], rounds: int, worry_level_decrease: Optional[bool] = True
) -> int:
    Monkey.monkeys = []
    Monkey.bulk_create(monkey_inputs)
    Monkey.run_rounds(rounds, worry_level_decrease)
    return Monkey.most_active_monkeys()
