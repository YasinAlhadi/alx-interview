#!/usr/bin/python3
""" locked boxes """


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened """
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
