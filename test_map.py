"""Unit test for map module"""
import unittest
from map import Map


class TestMap(unittest.TestCase):

    def test_init(self):
        self.map = Map((100, 100))
        self.assertEqual(100, len(self.map.nodes))
        self.assertEqual(100, len(self.map.nodes[0]))
        self.assertEqual((9, 9), self.map[9, 9].loc)
        self.assertEqual((0, 0), self.map[0, 0].loc)


if __name__ == '__main__':

    pass

