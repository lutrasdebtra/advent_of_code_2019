from typing import List, Iterable, Tuple
import re
from itertools import groupby, zip_longest


def _parse_almanac_maps(almanac: List[str]) -> List[List[List[Tuple[int, int]]]]:
    almanac_ranges = list(list() for _ in range(7))
    almanac.pop(0)  # Remove first empty line.
    almanac_maps = list(
        list(g) for k, g in groupby(almanac, key=lambda x: x != "") if k
    )

    for i, almanac_map in enumerate(almanac_maps):
        almanac_map.pop(0)  # Remove text.
        for j, item in enumerate(almanac_map):
            almanac_map[j] = [int(x) for x in re.findall(r"\d+", almanac_map[j])]
            destination, source, range_length = almanac_map[j]
            almanac_ranges[i].append(
                [
                    (source, source + range_length - 1),
                    (destination, destination + range_length - 1),
                ]
            )
    return almanac_ranges


def _calculate_lowest_location(almanac: List[str], seeds: Iterable[int]) -> int:
    lowest_location = None
    almanac_ranges = _parse_almanac_maps(almanac=almanac)

    for seed in seeds:
        loc = seed
        for almanac_range_group in almanac_ranges:
            for source_range, destination_range in almanac_range_group:
                if source_range[0] <= loc <= source_range[1]:
                    diff = loc - source_range[0]
                    loc = destination_range[0] + diff
                    break
        if not lowest_location or loc < lowest_location:
            lowest_location = loc

    return lowest_location


def calculate_lowest_location_seed_numbers(almanac: List[str]) -> int:
    seeds = [int(x) for x in re.findall(r"\d+", almanac.pop(0))]
    return _calculate_lowest_location(almanac=almanac, seeds=seeds)


def calculate_lowest_location_seed_ranges(almanac: List[str]) -> int:
    seeds = [int(x) for x in re.findall(r"\d+", almanac.pop(0))]
    seed_ranges = list(zip_longest(*[iter(seeds)] * 2))
    lowest_values = []
    for start, end in seed_ranges:
        # Use Generator ranges to avoid out of memory errors.
        lowest_values.append(
            _calculate_lowest_location(almanac=almanac, seeds=range(start, start + end))
        )
    return min(lowest_values)
