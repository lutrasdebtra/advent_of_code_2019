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
    return (x_start, y_start), grid


def find_crossovers(grid):
    return zip(*np.where(grid == 3))


def find_distance(grid, start):
    min_dist = 1000000000
    start_x, start_y = start
    for x, y in find_crossovers(grid):
        distance = abs(x - start_x) + abs(y - start_y)
        min_dist = distance if distance < min_dist else min_dist
    return min_dist


def closest_distance(wire_1, wire_2):
    wire_1_list = wire_1.split(',')
    wire_2_list = wire_2.split(',')
    print('generating grid')
    grid = generate_grid(wire_1_list, wire_2_list)
    print('populating grid')
    start, grid = populate_grid(wire_1_list, wire_2_list, grid)
    print('finding distance')
    return find_distance(grid, start)
