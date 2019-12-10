from challenge_3 import closest_distance, best_intersection


with open("three.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line.strip())
    wire_1, wire_2 = array[0], array[1]
print(closest_distance(wire_1, wire_2))
print(best_intersection(wire_1, wire_2))
