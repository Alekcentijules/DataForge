from typing import Tuple, List

def parse_input(user_input: str) -> Tuple[str, List[str]]:
    parts = user_input.strip().split()
    if not parts:
        return ()
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args

