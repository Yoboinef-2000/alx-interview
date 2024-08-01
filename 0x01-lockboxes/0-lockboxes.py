#!/usr/bin/python3

"""Unlock the boxes. Free up all my Bs."""


def canUnlockAll(boxes):
    """This problem took me longer to understand than to solve."""
    unlockedBoxes = [0]
    totalBoxes = len(boxes)

    i = 0
    while i < len(unlockedBoxes):
        for aKey in boxes[unlockedBoxes[i]]:
            if aKey not in unlockedBoxes and aKey < totalBoxes:
                unlockedBoxes.append(aKey)
        i += 1

    if len(unlockedBoxes) == totalBoxes:
        return True
    return False
