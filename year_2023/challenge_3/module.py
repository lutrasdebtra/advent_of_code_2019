from typing import List, Tuple, Dict
import math


class EngineSchematic:
    def __init__(self, engine_schematic: List[List[str]]):
        self.engine_schematic: List[List[str]] = engine_schematic
        self.parts_numbers: List[int] = []
        self.gear_coords: List[Tuple[int, int]] = []
        self.parts_number_coords: Dict[Tuple[int, int], int] = {}

    def _is_part_number(self, x: int, y: int, number_length: int) -> bool:
        check_coords = [
            (x, y + 1),
            (x, y - number_length),
            (x - 1, y),
            (x - 1, y + 1),
            (x + 1, y),
            (x + 1, y + 1),
        ]
        # Distance to check back is length of number + 1
        # i.e. 592 where 2 is position 4: [4 - 1, 4 - 2, 4 - 3]
        for offset in range(1, number_length + 1):
            check_coords.extend(
                [
                    (x - 1, y - offset),
                    (x + 1, y - offset),
                ]
            )

        for x_2, y_2 in check_coords:
            if x_2 < 0 or y_2 < 0:
                continue
            try:
                curr_value = self.engine_schematic[x_2][y_2]
                if not (curr_value.isdigit() or curr_value == "."):
                    return True
            except IndexError:
                continue
        return False

    def _store_num_data(self, number_buffer: str, x: int, y: int) -> None:
        num = int(number_buffer)
        self.parts_numbers.append(num)
        # Capture all coords of number starting at the end.
        for offset in range(0, len(number_buffer)):
            self.parts_number_coords[(x, y - offset)] = num

    def _process_schematic(self) -> None:
        number_buffer = ""
        num_x, num_y = 0, 0
        for x in range(len(self.engine_schematic)):
            if number_buffer:
                if self._is_part_number(
                    x=num_x, y=num_y, number_length=len(number_buffer)
                ):
                    self._store_num_data(number_buffer=number_buffer, x=num_x, y=num_y)
            number_buffer = ""
            for y in range(len(self.engine_schematic[x])):
                curr_value = self.engine_schematic[x][y]
                if curr_value.isdigit():
                    number_buffer += curr_value
                    num_x, num_y = x, y
                else:
                    if number_buffer:
                        if self._is_part_number(
                            x=num_x, y=num_y, number_length=len(number_buffer)
                        ):
                            self._store_num_data(
                                number_buffer=number_buffer, x=num_x, y=num_y
                            )
                        number_buffer = ""
                    if curr_value == "*":
                        self.gear_coords.append((x, y))

    def sum_part_numbers(self) -> int:
        if not self.parts_numbers:
            self._process_schematic()
        return sum(self.parts_numbers)

    def sum_gear_ratios(self) -> int:
        if not self.gear_coords:
            self._process_schematic()
        gear_ratio_sum = 0
        for x, y in self.gear_coords:
            check_coords = [
                (x, y + 1),
                (x, y - 1),
                (x + 1, y),
                (x - 1, y),
                (x + 1, y + 1),
                (x + 1, y - 1),
                (x - 1, y + 1),
                (x - 1, y - 1),
            ]
            adjacent_parts_numbers = set()
            for x_2, y_2 in check_coords:
                if (x_2, y_2) in self.parts_number_coords:
                    adjacent_parts_numbers.add(self.parts_number_coords[(x_2, y_2)])
            if len(adjacent_parts_numbers) == 2:
                gear_ratio_sum += math.prod(adjacent_parts_numbers)
        return gear_ratio_sum
