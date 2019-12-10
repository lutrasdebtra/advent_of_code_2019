import math


def fuel_requirements_fuel_inclusive(f_r):
    fuel_list = []
    while True:
        f_r = math.floor(f_r / 3.0) - 2
        if f_r > 0:
            fuel_list.append(f_r)
        else:
            break
    return sum(fuel_list)
