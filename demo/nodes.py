"""This file creates 100 nodes in a 10*10 square space"""
from __future__ import annotations
from typing import Tuple, Optional


class Node:
    """A Node in a map.

    === Attributes ===
    can_pass:
        indicate if a tree can pass through this node
    loc:
        x, y location of this node in a map
    up:
        the node that has the same x value but y value is larger by by 1
    down:
        the node that has the same x value but y value is smaller by 1
    left:
        the node that has the same y value but x value is smaller by 1
    right:
        the node that has the same y value but x value is larger by 1
    """
    can_pass: bool
    loc: Tuple[int, int]
    up: Optional[Node]
    down: Optional[Node]
    left: Optional[Node]
    right: Optional[Node]

    def __init__(self, location: Tuple[int, int]) -> None:
        """Initialize a node and set can_pass to be True"""
        self.loc = location
        self.can_pass = True
        self.up = None
        self.down = None
        self.left = None
        self.right = None
