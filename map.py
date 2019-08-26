"""This is the implementation for <Map>"""
from __future__ import annotations
from typing import List, Tuple
from numpy import array
from node import Node


class Map:
    """A <Map> object is consisted of many <Node> instances

    === Attributes ===
    Nodes:
        A list of list of nodes. Each nested list represents a column of nodes
        on a map. The first nested list represents the first column, the second
        represents the second column,....
    """
    Nodes: array

    def __init__(self, size: Tuple[int, int]) -> None:
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
        pass

    def __getitem__(self, item: Tuple[int, int]) -> Node:
        """return node at position <item> on a map"""
        pass

    def _generate_nodes_array(self) -> array:
        """This helper method generates as many nodes as required in size.
        Each node in created array is not connected to any other nodes
        """
        pass

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
