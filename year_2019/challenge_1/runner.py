from year_2019.challenge_1 import fuel_requirements, fuel_requirements_fuel_inclusive

with open("one.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(fuel_requirements(int(line)))
print(sum(array))

with open("one.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(fuel_requirements_fuel_inclusive(int(line)))
print(sum(array))
