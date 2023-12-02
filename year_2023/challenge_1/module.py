from typing import List


def _replace_text_numbers(calibration_document: List[str]) -> List[str]:
    # Allow for overlapping numbers ("eighthree" is 83) by including the letters around the substitution:
    # eighthree -> e8three -> e8t3e -> 83
    patterns = [
        ("one", "o1e"),
        ("two", "t2o"),
        ("three", "t3e"),
        ("four", "f4r"),
        ("five", "f5e"),
        ("six", "s6x"),
        ("seven", "s7n"),
        ("eight", "e8t"),
        ("nine", "n9e"),
    ]
    # Join document back into a single string to avoid an additional loop.
    joined_calibration_document = " ".join(calibration_document)
    for p in patterns:
        joined_calibration_document = joined_calibration_document.replace(*p)

    return joined_calibration_document.split(" ")


def find_calibration_value(
    calibration_document: List[str], replace_text_numbers: bool = False
) -> int:
    calibration_value = 0

    if replace_text_numbers:
        calibration_document = _replace_text_numbers(
            calibration_document=calibration_document
        )
    for calibration_line in calibration_document:
        calibration_digits = []
        for char in calibration_line:
            if char.isdigit():
                calibration_digits.append(char)
        calibration_value += int(f"{calibration_digits[0]}{calibration_digits[-1]}")
    return calibration_value
