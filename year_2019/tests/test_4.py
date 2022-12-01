import pytest

from year_2019.challenge_4 import valid_password


@pytest.mark.parametrize(
    "num, bool_",
    [
        (111111, True),
        (122345, True),
        (111123, True),
        (135679, False),
        (223450, False),
        (123789, False),
    ],
)
def test_valid_password(num, bool_):
    assert valid_password(num) == bool_


@pytest.mark.parametrize(
    "num, bool_",
    [
        (112233, True),
        (123444, False),
        (111122, True),
    ],
)
def test_valid_password_additional_param(num, bool_):
    assert valid_password(num, additional_check=True) == bool_
