from year_2022.challenge_13.module import packet_order, packet_sort

with open("thirteen.txt", "r") as ins:
    packets = []
    for line in ins:
        packets.append(line.strip())
    print(packet_order(packets))
    print(packet_sort(packets))
