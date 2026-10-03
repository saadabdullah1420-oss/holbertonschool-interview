#!/usr/bin/python3


def canUnlockAll(boxes):
    """Determine if all boxes can be opened."""
    opened = {0}
    stack = [0]

    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if key < len(boxes) and key not in opened:
                opened.add(key)
                stack.append(key)

    return len(opened) == len(boxes)
