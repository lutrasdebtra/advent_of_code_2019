from typing import Text


def buffer_processor(communication_stream: Text, marker: int) -> int:
    for i in range(len(communication_stream)):
        chunk = set(communication_stream[i : i + marker])
        if len(chunk) == marker:
            return i + marker
