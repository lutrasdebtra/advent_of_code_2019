import re
from typing import List, Text, Optional


def crane_controls(instructions: List[Text], bulk_move: Optional[bool] = False) -> Text:
    box_data, stack_count_data, move_data = [], "", []
    for line in instructions:
        if bool(re.match(r"\[\w", line.strip())):
            box_data.append(line)
        elif bool(re.match(r"\d{1}\s{3}", line.strip())):
            stack_count_data = line
        elif line.startswith("move"):
            move_data.append(line)

    stacks = [list() for _ in range(int(stack_count_data.strip()[-1]))]
    stack_pos = {
        idx: int(x) - 1 for idx, x in enumerate(stack_count_data) if x.isdigit()
    }

    for line in reversed(box_data):
        for idx, c in enumerate(line):
            if bool(re.match(r"\w", c)):
                stacks[stack_pos[idx]].append(c)

    for m in move_data:
        m_count, m_from, m_to = re.findall(r"\d+", m)
        m_count, m_from, m_to = int(m_count), int(m_from) - 1, int(m_to) - 1
        # P1
        if not bulk_move:
            for _ in range(m_count):
                tmp = stacks[m_from].pop()
                stacks[m_to].append(tmp)
        # P2
        else:
            tmp = stacks[m_from][-m_count:]
            del stacks[m_from][-m_count:]
            stacks[m_to].extend(tmp)

    return "".join(s[-1] for s in stacks)
