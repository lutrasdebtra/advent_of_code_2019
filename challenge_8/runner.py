from challenge_8 import corrupt_check, render_image

with open("eight.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line.strip())
bits = array[0]

print(corrupt_check(bits, 25, 6))
print(list(render_image(bits, 25, 6)))

