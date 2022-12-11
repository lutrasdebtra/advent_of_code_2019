import pytest

from year_2022.challenge_11.module import Monkey, find_active_monkeys


@pytest.fixture
def monkey_0_input():
    data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
    """
    return data.splitlines()


@pytest.fixture
def monkey_inputs():
    data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
    """
    return data.splitlines()


def test_monkey_init(monkey_0_input):
    Monkey.monkeys = []
    m_0 = Monkey(monkey_0_input)
    assert m_0.items == [79, 98]
    assert m_0.operation == "old * 19"
    assert m_0.divisible_by == 23
    assert m_0.divisible_by_true_monkey == 2
    assert m_0.divisible_by_false_monkey == 3


def test_first_round(monkey_inputs):
    Monkey.monkeys = []
    Monkey.bulk_create(monkey_inputs)
    Monkey.run_rounds(1)
    assert [m.items for m in Monkey.monkeys] == [
        [20, 23, 27, 26],
        [2080, 25, 167, 207, 401, 1046],
        [],
        [],
    ]


@pytest.mark.parametrize(
    "rounds, worry_level_decrease, expected",
    [
        (20, True, [101, 95, 7, 105]),
        (1, False, [2, 4, 3, 6]),
        (20, False, [99, 97, 8, 103]),
        (1000, False, [5204, 4792, 199, 5192]),
        (10000, False, [52166, 47830, 1938, 52013]),
    ],
)
def test_twenty_rounds_no_worry_level_decrease(
    monkey_inputs, rounds, worry_level_decrease, expected
):
    Monkey.monkeys = []
    Monkey.bulk_create(monkey_inputs)
    Monkey.run_rounds(rounds, worry_level_decrease)
    assert [monkey.inspection_count for monkey in Monkey.monkeys] == expected


def test_find_active_monkeys(monkey_inputs):
    assert find_active_monkeys(monkey_inputs, 20) == 10605


def test_find_active_monkeys_no_worry_level_decrease(monkey_inputs):
    assert (
        find_active_monkeys(monkey_inputs, 10000, worry_level_decrease=False)
        == 2713310158
    )
