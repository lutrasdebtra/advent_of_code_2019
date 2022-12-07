from year_2022.challenge_6.module import buffer_processor

with open("six.txt", "r") as ins:
    communication_stream = ins.readline()
    print(buffer_processor(communication_stream, 4))
    print(buffer_processor(communication_stream, 14))
