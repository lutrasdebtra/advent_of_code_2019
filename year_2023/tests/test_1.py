import pytest

from year_2023.challenge_1.module import find_calibration_value


@pytest.mark.parametrize(
    "calibration_document, replace_text_numbers, calibration_value",
    [
        (
            [
                "1abc2",
                "pqr3stu8vwx",
                "a1b2c3d4e5f",
                "treb7uchet",
            ],
            False,
            142,
        ),
        (["eighthree"], True, 83),
        (["sevenine"], True, 79),
        (
            [
                "two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen",
            ],
            True,
            281,
        ),
    ],
)
def test_find_calibration_value(
    calibration_document, replace_text_numbers, calibration_value
):
    assert (
        find_calibration_value(
            calibration_document, replace_text_numbers=replace_text_numbers
        )
        == calibration_value
    )
