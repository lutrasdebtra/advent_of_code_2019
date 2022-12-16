import re
from typing import List, Text
from scipy.spatial.distance import cityblock


def beacon_position(sensor_input: List[Text], y_calc: int) -> int:
    beacons = set()
    sensor_zones = set()
    covered_y = 0
    for line in sensor_input:
        sensor_x, sensor_y, beacon_x, beacon_y = map(int, re.findall(r"[-]?\d+", line))
        manhattan_dist = cityblock((sensor_x, sensor_y), (beacon_x, beacon_y))
        beacons.add((beacon_x, beacon_y))
        sensor_zones.add((sensor_x, sensor_y))
        sensor_x_max, sensor_x_min = (
            sensor_x + manhattan_dist,
            sensor_x - manhattan_dist,
        )
        sensor_y_max, sensor_y_min = (
            sensor_y + manhattan_dist,
            sensor_y - manhattan_dist,
        )
        width = 0
        for x in range(sensor_x_min, sensor_x_max + 1):
            for w in range(-width, width + 1):
                sensor_zones.add((x, sensor_y + w))
            if x < sensor_x:
                width += 1
            else:
                width -= 1
    for x, y in sensor_zones:
        if y == y_calc and (x, y) not in beacons:
            covered_y += 1
    return covered_y
