#!/usr/bin/python3
"""
Unlocks lists of lists using canUnlockAll function
"""


def canUnlockAll(boxes):
    """
    A method that determines if all the boxes can be opened
    """
    visited_boxes = [0]

    for box in visited_boxes:
        keys = boxes[box]
        for key in keys:
            if key not in visited_boxes and key < len(boxes):
                visited_boxes.append(key)

    return len(visited_boxes) == len(boxes)
