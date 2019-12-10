import numpy as np


def find_biggest_length(wire):
    directions = {
        'U': 0,
        'D': 0,
        'R': 0,
        'L': 0,
    }
    for direction in wire:
        direction, dist = direction[0], int(direction[1:])
        directions[direction] += dist
    return max(directions.values())


def generate_grid(wire_1, wire_2):
    size_ = max(find_biggest_length(wire_1), find_biggest_length(wire_2))
    return np.zeros((size_*3, size_*3))


def populate_grid(wire_1, wire_2, grid):
    cross_overs = []
    x, y = grid.shape
    x /= 2
    y /= 2
    x_start = int(x)
    y_start = int(y)
    for index, wire in enumerate([wire_1, wire_2]):
        wire_num = index + 1
        x = x_start
        y = y_start
        for instruction in wire:
            direction, dist = instruction[0], int(instruction[1:])
            for i in range(1, dist+1):
                if direction == 'U':
                    y += 1
                elif direction == 'D':
                    y -= 1
                elif direction == 'R':
                    x += 1
                elif direction == 'L':
                    x -= 1
                grid[x][y] += wire_num
                if grid[x][y] == 3:
                    cross_overs.append((x, y))
    return (x_start, y_start), grid, cross_overs


def find_distance(cross_overs, start):
    min_dist = 1000000000
    start_x, start_y = start
    for x, y in cross_overs:
        distance = abs(x - start_x) + abs(y - start_y)
        min_dist = distance if distance < min_dist else min_dist
    return min_dist


def closest_distance(wire_1, wire_2):
    wire_1_list = wire_1.split(',')
    wire_2_list = wire_2.split(',')
    grid = generate_grid(wire_1_list, wire_2_list)
    start, grid, cross_overs = populate_grid(wire_1_list, wire_2_list, grid)
    return find_distance(cross_overs, start)


def intersection_distance(wire_1, wire_2, start, cross_overs):
    distances = {}
    for index, wire in enumerate([wire_1, wire_2]):
        x = start[0]
        y = start[1]
        distance_to_intersection = 0
        for instruction in wire:
            direction, dist = instruction[0], int(instruction[1:])
            for i in range(1, dist+1):
                distance_to_intersection += 1
                if direction == 'U':
                    y += 1
                elif direction == 'D':
                    y -= 1
                elif direction == 'R':
                    x += 1
                elif direction == 'L':
                    x -= 1
                if (x, y) in cross_overs:
                    if (x, y) not in distances:
                        distances[(x, y)] = {0: 0, 1: 0}
                    distances[(x, y)][index] = distance_to_intersection
    return min(
        [(x[0] + x[1]) for x in distances.values()]
    )


def best_intersection(wire_1, wire_2):
    wire_1_list = wire_1.split(',')
    wire_2_list = wire_2.split(',')
    grid = generate_grid(wire_1_list, wire_2_list)
    start, grid, cross_overs = populate_grid(wire_1_list, wire_2_list, grid)
    return intersection_distance(wire_1_list, wire_2_list, start, cross_overs)
