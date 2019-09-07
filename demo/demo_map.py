"""This module will create a 10 * 10 map using <Node> type"""
from nodes import Node


def create_nodes_in_a_column(start_column: int, num: int) -> list:
    nodes = []
    for y in range(num):
        nodes.append(Node((start_column, y)))
    connect_nodes_down(nodes)
    connect_nodes_up(nodes)

    return nodes


def connect_nodes_down(nodes: list) -> None:
    nodes_num = len(nodes)
    for i in range(nodes_num - 1):
        nodes[i].down = nodes[i + 1]


def connect_nodes_up(nodes: list) -> None:
    nodes_num = len(nodes)
    for i in reversed(range(1, nodes_num)):
        nodes[i].up = nodes[i - 1]


nodes0 = create_nodes_in_a_column(0, 10)
nodes1 = create_nodes_in_a_column(1, 10)
nodes2 = create_nodes_in_a_column(2, 10)
nodes3 = create_nodes_in_a_column(3, 10)
nodes4 = create_nodes_in_a_column(4, 10)
nodes5 = create_nodes_in_a_column(5, 10)
nodes6 = create_nodes_in_a_column(6, 10)
nodes7 = create_nodes_in_a_column(7, 10)
nodes8 = create_nodes_in_a_column(8, 10)
nodes9 = create_nodes_in_a_column(9, 10)

nodes_columns = [nodes0,
                 nodes1,
                 nodes2,
                 nodes3,
                 nodes4,
                 nodes5,
                 nodes6,
                 nodes7,
                 nodes8,
                 nodes9]


def connect_nodes_right(columns: list) -> None:
    height = len(columns[0])
    width = len(columns)

    for x in range(width - 1):
        for y in range(height):
            columns[x][y].right = columns[x + 1][y]


def connect_nodes_left(columns: list) -> None:
    height = len(columns[0])
    width = len(columns)

    for x in reversed(range(1, width)):
        for y in range(height):
            columns[x][y].left = columns[x - 1][y]


connect_nodes_left(nodes_columns)
connect_nodes_right(nodes_columns)
nodes_map = nodes_columns


if __name__ == "__main__":
    x, y = 7, 8
    print(nodes_columns[x][y].down is nodes_columns[x][y + 1],
          nodes_columns[x][y].up is nodes_columns[x][y - 1],
          nodes_columns[x][y].left is nodes_columns[x - 1][y],
          nodes_columns[x][y].right is nodes_columns[x + 1][y])
