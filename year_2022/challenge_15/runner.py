from year_2022.challenge_15.module import beacon_position

with open("fithteen.txt", "r") as ins:
    sensor_input = []
    for line in ins:
        sensor_input.append(line.strip())
    print(beacon_position(sensor_input, 2000000))
