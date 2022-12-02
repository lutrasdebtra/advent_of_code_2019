from typing import Text, List, Tuple

DECRYPTION_GUIDE = {"A": "R", "B": "P", "C": "S", "X": "R", "Y": "P", "Z": "S"}

R_P_S_COUNTERS = {"R": "S", "P": "R", "S": "P"}

R_P_S_COUNTERS_REVERSED = {v: k for k, v in R_P_S_COUNTERS.items()}

POINTS = {"R": 1, "P": 2, "S": 3}

WIN_POINTS = 6
DRAW_POINTS = 3


def _score_calculation_1(opponent: Text, you: Text) -> int:
    score = POINTS[you]
    if you == opponent:
        score += DRAW_POINTS
    if R_P_S_COUNTERS[you] == opponent:
        score += WIN_POINTS
    return score


def calculate_tournament_1(encrypted_guide: List[Tuple[Text, Text]]) -> int:
    final_score = 0
    for rnd in encrypted_guide:
        opponent, you = DECRYPTION_GUIDE[rnd[0]], DECRYPTION_GUIDE[rnd[1]]
        final_score += _score_calculation_1(opponent=opponent, you=you)
    return final_score


def _score_calculation_2(opponent: Text, desired_result: Text) -> int:
    score = 0
    # Draw - Y
    if desired_result == "Y":
        score += POINTS[opponent] + DRAW_POINTS
    # Lose - X
    elif desired_result == "X":
        score += POINTS[R_P_S_COUNTERS[opponent]]
    # Win - Z
    elif desired_result == "Z":
        score += POINTS[R_P_S_COUNTERS_REVERSED[opponent]] + WIN_POINTS
    return score


def calculate_tournament_2(encrypted_guide: List[Tuple[Text, Text]]) -> int:
    final_score = 0
    for rnd in encrypted_guide:
        opponent, desired_result = DECRYPTION_GUIDE[rnd[0]], rnd[1]
        final_score += _score_calculation_2(
            opponent=opponent, desired_result=desired_result
        )
    return final_score
