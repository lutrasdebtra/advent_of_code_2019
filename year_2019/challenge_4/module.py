from itertools import groupby


def _check_length(num):
    return len(str(num)) == 6


def _check_adjacency(num):
    digits = [int(x) for x in str(num)]
    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1]:
            return True
    return False


def _check_incrementality(num):
    digits = [int(x) for x in str(num)]
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return False
    return True


def _check_adjacency_length(num):
    digits = [int(x) for x in str(num)]
    if any([sum(1 for _ in group) == 2 for _, group in groupby(digits)]):
        return True
    return False


def valid_password(num, additional_check=False):
    valid = _check_length(num) and _check_adjacency(num) and _check_incrementality(num)
    if additional_check:
        valid = valid and _check_adjacency_length(num)
    return valid
