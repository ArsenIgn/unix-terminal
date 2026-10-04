import os
import shlex

def parse_command(user_input):
    expanded_input = os.path.expandvars(user_input)

    try:
        parts = shlex.split(expanded_input)
    except ValueError:
        raise ValueError("Не удалось разобрать команду")

    if not parts:
        return "", []

    command = parts[0]
    args = parts[1:]

    return command, args