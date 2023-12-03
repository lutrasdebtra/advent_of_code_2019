from year_2023.challenge_3.module import EngineSchematic

with open("three.txt", "r") as ins:
    engine_schematic = []
    for line in ins:
        engine_schematic.append(list(line.strip()))
    print(EngineSchematic(engine_schematic=engine_schematic).sum_part_numbers())
    print(EngineSchematic(engine_schematic=engine_schematic).sum_gear_ratios())
