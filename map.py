"""This is the implementation for <Map>"""
from __future__ import annotations
from typing import List, Tuple, Optional

"""Implementation for Node class"""


class Node:
    """A <Node> class should have at least three other nodes or maximum 8 other
    nodes connect to it from different directions. A <Node> instance can either
    work like a barrier or a path
    """
    left: Optional[Node]
    up: Optional[Node]
    right: Optional[Node]
    down: Optional[Node]
    lu: Optional[Node]
    ru: Optional[Node]
    rd: Optional[Node]
    ld: Optional[Node]
    can_pass: bool
    loc: Tuple[int, int]

    def __init__(self, loc: Tuple[int, int], can_pass: bool = True) -> None:
        """Initializa a <Node> instance whose can_pass attrubute is set as
        requested. Otherwise, set it to True by default.
        """
        self.can_pass = can_pass
        self.left = None
        self.up = None
        self.right = None
        self.down = None
        self.lu = None
        self.ru = None
        self.rd = None
        self.ld = None
        self.loc = loc


class Map:
    """A <Map> object is consisted of many <Node> instances

    === Attributes ===
    nodes:
        A list of list of nodes. Each nested list represents a column of nodes
        on a map. The first nested list represents the first column, the second
        represents the second column,....
    barriers:
        This is a list of tuples that indicates which nodes are supposed to be
        barriers when a map is being initilized.
    size:
        A tuple that indicates the size of a map
    """
    nodes: List[List[Node]]
    barriers: Optional[List[Tuple]]

    def __init__(self, size: Tuple[int, int],
                 barriers: Optional[List[Tuple[int, int]]] = None) -> None:
        """Create certain amount of nodes based on the size given. After nodes
        are created, nodes should be connected in their right order.

        For a centre node who has eight neighboring nodes available, its
        neighboring nodes'(x, y) parameters should change following
        the rules below:

            Relative to the centre node who has x value <x> and y value <y>:
             its <left> node should have (x - 1, y) as position parameters.
             its <right> node should have (x + 1, y) as position parameters.
             its <up> node should have (x, y - 1) as position parameters.
             its <down> node should have (x, y + 1) as position parameters.
             its <lu> node should have (x - 1, y - 1) as position parameters.
             its <ru> node should have (x + 1, y - 1) as position parameters.
             its <rd> node should have (x + 1, y + 1) as position parameters.
             its <ld> node should have (x - 1, y + 1) as position parameters.
        """
        self.barriers = barriers
        self.size = size
        self.nodes = self._generate_nodes_lists()

    def __getitem__(self, item: Tuple[int, int]) -> Node:
        """return node at position <item> on a map"""
        return self.nodes[item[0]][item[1]]

    def _generate_nodes_lists(self) -> List[List[Node]]:
        """This helper method generates as many nodes as required in size.
        Each node in created array is not connected to any other nodes
        """
        columns = []
        if self.barriers is None:
            for x in range(self.size[0]):
                column = []
                for y in range(self.size[1]):
                    column.append(Node((x, y)))
                columns.append(column)
        else:
            for x in range(self.size[0]):
                column = []
                for y in range(self.size[1]):
                    if (x, y) in self.barriers:
                        column.append(Node((x, y), False))
                    else:
                        column.append(Node((x, y)))
                columns.append(column)
        return columns

    def _connect_left_nodes(self) -> None:
        """This helper method connects each node's left node if available
        """
        pass

    def _connect_right_nodes(self) -> None:
        """This helper method connects each node's right node if available
        """
        pass

    def _connect_up_nodes(self) -> None:
        """This helper method connects each node's up node if available
        """
        pass

    def _connect_down_nodes(self) -> None:
        """This helper method connects each node's down node if available
        """
        pass

    def _connect_lu_nodes(self) -> None:
        """This helper method connects each node's lu node if available
        """
        pass

    def _connect_ru_nodes(self) -> None:
        """This helper method connects each node's ru node if available
        """
        pass

    def _connect_rd_nodes(self) -> None:
        """This helper method connects each node's rd node if available
        """
        pass

    def _connect_ld_nodes(self) -> None:
        """This helper method connects each node's ld node if available
        """
        pass


