import pytest

from year_2023.challenge_15.module import run_hash_algorithm, calculate_focal_lengths


@pytest.mark.parametrize(
    "init_sequence, result",
    [("HASH", 52), ("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7", 1320)],
)
def test_run_hash_algorithm(init_sequence, result):
    assert run_hash_algorithm(init_sequence=init_sequence) == result


def test_calculate_focal_lengths():
    init_sequence = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    assert calculate_focal_lengths(init_sequence=init_sequence) == 145
