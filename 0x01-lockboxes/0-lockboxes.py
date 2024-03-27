#!/usr/bin/python3
"""
Lockboxes
Checks if each box can be unlocked from n boxes.
Boxes are numbered from 0 to n - 1 sequentially,
and each box might contain keys to other boxes.
"""

def canUnlockAll(boxes):
    """
    Determines whether all the boxes can be unlocked.
    Args:
    boxes: A list of lists, where each inner list represents a box,
    and the elements of the inner list represent the keys to other boxes.
    Returns:
    True if all the boxes can be opened, otherwise False.
    """
    opened_boxes = [False] * len(boxes)
    opened_boxes[0] = True
    next_box = [0]

    # perform depth-first search
    while next_box:
        current_box = next_box.pop()
        for key in boxes[current_box]:
            if key >= 0 and key < len(boxes) and not opened_boxes[key]:
                next_box.append(key)
                opened_boxes[key] = True

    # check if all boxes have been visited
    return all(opened_boxes)
