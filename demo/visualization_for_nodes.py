import pygame as pg
from demo_map import nodes_map, Node
from typing import Tuple, List
from random import randint

pg.init()


def get_nodes_position(node: Node,
                       ox: int,
                       oy: int,
                       sqr_len: int) -> Tuple[int, int]:
    """return nodes position in a pygame window"""
    x_pos = ox + node.loc[0] * sqr_len
    y_pos = oy + node.loc[1] * sqr_len
    return x_pos, y_pos


def get_screen_size(ox: int,
                    oy: int,
                    nodes_map: List[List[Node]],
                    sqr_len: int) -> Tuple[int, int]:
    """Return screen size using starting x and y axises and the size of
    <nodes_map> and each nodes square len"""
    width = ox + len(nodes_map) * sqr_len
    height = oy + len(nodes_map[0]) * sqr_len
    return width, height


def which_node(mouse_x: int, mouse_y: int) -> Tuple[int, int]:
    """return cursor is currently on which node"""
    node_x = (mouse_x - ox) // sqr_len
    node_y = (mouse_y - oy) // sqr_len
    return node_x, node_y


def get_quit_button_rect(ox: int,
                         screen_height: int) -> pg.Rect:
    """Using original x axis and screen height to get where quit button should
    be
    """
    left = int(ox * (1 / 5))
    right = int(ox * (4 / 5))
    top = int(screen_height * (44 / 50))
    bottom = int(screen_height * (48 / 50))
    return pg.Rect(left, top, right - left, bottom - top)


ox, oy = 100, 0
sqr_len = 40
blue = (66, 135, 245)
tile_edge_color = (245, 173, 66)
tile_color = (245, 203, 66)
white = (255, 255, 255)
green = (172, 219, 121)
red = (245, 96, 66)
clock = pg.time.Clock()
fps = 10

scree_width, screen_height = get_screen_size(ox, oy, nodes_map, sqr_len)
quit_rect = get_quit_button_rect(ox, screen_height)

grass = pg.image.load('grass.jpg')
wall = pg.image.load('wall.jpg')
grass = pg.transform.scale(grass, (sqr_len, sqr_len))
wall = pg.transform.scale(wall, (sqr_len, sqr_len))
font = pg.font.SysFont(None, 25)
quit_msg = font.render('Quit', True, white)


def main():
    pg.display.set_caption('Demo Map')
    screen = pg.display.set_mode((scree_width, screen_height))
    screen.fill(blue)
    screen.fill(red, quit_rect)
    screen.blit(quit_msg,
                [quit_rect.left + quit_rect.width / 2 - quit_msg.get_size()[
                    0] / 2,
                 quit_rect.top + quit_rect.height / 2 - quit_msg.get_size()[
                     1] / 2])

    node_rects = []
    for node_column in nodes_map:
        rect_column = []
        for node in node_column:
            x_pos, y_pos = get_nodes_position(node, ox, oy, sqr_len)
            rect = pg.Rect(x_pos, y_pos, sqr_len, sqr_len)
            # screen.fill(tile_color, rect)
            # rect_column.append(pg.draw.rect(screen, tile_color,
            # rect))
            rect_column.append(screen.blit(grass, rect))

            pg.display.update()
            # pg.event.get()
            # clock.tick(10)

        node_rects.append(rect_column)

    assert type(node_rects) is list
    for column in node_rects:
        assert type(column) is list
        for rect in column:
            assert type(rect) is pg.Rect

    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

            if event.type == pg.MOUSEBUTTONDOWN:
                button = pg.mouse.get_pressed()
                mouse_x, mouse_y = pg.mouse.get_pos()
                if mouse_x >= ox and mouse_y >= oy:
                    node_x, node_y = which_node(mouse_x, mouse_y)
                    if button[0]:
                        if nodes_map[node_x][node_y].can_pass:
                            nodes_map[node_x][node_y].can_pass = False
                            rect = node_rects[node_x][node_y]
                            screen.blit(wall, rect)
                            pg.display.update(rect)
                        elif not nodes_map[node_x][node_y].can_pass:
                            nodes_map[node_x][node_y].can_pass = True
                            rect = node_rects[node_x][node_y]
                            screen.blit(grass, rect)
                            pg.display.update(rect)
                else:
                    if quit_rect.left <= mouse_x <= quit_rect.left + quit_rect.width and \
                            quit_rect.top <= mouse_y <= quit_rect.top + quit_rect.height:
                        done = True


if __name__ == '__main__':

    x, y = 8, 8
    assert nodes_map[x][y].down is nodes_map[x][y + 1]
    assert nodes_map[x][y].up is nodes_map[x][y - 1]
    assert nodes_map[x][y].left is nodes_map[x - 1][y]
    assert nodes_map[x][y].right is nodes_map[x + 1][y]

    main()
    pg.quit()
