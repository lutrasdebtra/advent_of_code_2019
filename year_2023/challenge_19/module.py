from typing import List, Dict, Tuple, Generator
from itertools import groupby
import re

STARTER_WORKFLOW = "in"


def _generate_workflow_dict(workflows: List[str]) -> Dict[str, List[Tuple[str, str]]]:
    workflows_dict = {}
    workflow_strings, _ = [
        list(y) for x, y in groupby(workflows, lambda z: z == "") if not x
    ]

    for workflow in workflow_strings:
        workflow = workflow[:-1]  # Remove }.
        name, workflow = workflow.split("{")
        individual_workflows = workflow.split(",")
        else_case = individual_workflows.pop()
        workflow_steps = []
        for individual_workflow in individual_workflows:
            func, result = individual_workflow.split(":")
            workflow_steps.append((func, result))
        workflow_steps.append(("True", else_case))
        workflows_dict[name] = workflow_steps

    return workflows_dict


def _process_part(
    part: Dict[str, int], workflows_dict: Dict[str, List[Tuple[str, str]]]
) -> str:
    result = STARTER_WORKFLOW
    x, m, a, s = part.values()
    while result not in ["A", "R"]:
        workflow_steps = workflows_dict[result]
        for func, new_result in workflow_steps:
            if eval(func):
                result = new_result
                break
    return result


def calculate_accepted_ratings(workflows: List[str]) -> int:
    workflows_dict = _generate_workflow_dict(workflows=workflows)
    parts = []

    _, parts_strings = [
        list(y) for x, y in groupby(workflows, lambda z: z == "") if not x
    ]

    for part in parts_strings:
        part_numbers = [int(x) for x in re.findall(r"\d+", part)]
        parts.append(
            {
                "x": part_numbers[0],
                "m": part_numbers[1],
                "a": part_numbers[2],
                "s": part_numbers[3],
            }
        )

    total_accepted_ratings = 0
    for part in parts:
        result = _process_part(part=part, workflows_dict=workflows_dict)
        if result == "A":
            total_accepted_ratings += sum(part.values())
    return total_accepted_ratings


def _generate_parts_combinations() -> Generator[Dict[str, int], None, None]:
    for x in range(1, 4001):
        print(x)
        for m in range(1, 4001):
            for a in range(1, 4001):
                for s in range(1, 4001):
                    yield {"x": x, "m": m, "a": a, "s": s}


def calculate_possible_accepted_parts(workflows: List[str]) -> int:
    workflows_dict = _generate_workflow_dict(workflows=workflows)

    possible_accepted_combinations = 0
    for part in _generate_parts_combinations():
        result = _process_part(part, workflows_dict=workflows_dict)
        if result == "A":
            possible_accepted_combinations += 1
    return possible_accepted_combinations
