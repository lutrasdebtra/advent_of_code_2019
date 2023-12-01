from year_2023.challenge_1.module import find_calibration_value

with open("one.txt", "r") as ins:
    calibration_document = []
    for line in ins:
        calibration_document.append(line.strip())
    print(find_calibration_value(calibration_document=calibration_document))
    print(
        find_calibration_value(
            calibration_document=calibration_document, replace_text_numbers=True
        )
    )
