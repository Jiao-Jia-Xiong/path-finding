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
        self.assertEqual((0, 9), self.map[0, 9].loc)
        self.assertEqual((9, 0), self.map[9, 0].loc)

    def test_init_with_barriers(self):
        self.barriers = [(0, 1), (5, 5), (5, 6), (76, 68), (99, 99)]
        self.map = Map((100, 100), self.barriers)
        self.assertFalse(self.map[5, 6].can_pass)
        self.assertFalse(self.map[76, 68].can_pass)
        self.assertFalse(self.map[99, 99].can_pass)
        self.assertTrue(self.map[78, 76].can_pass)
        self.assertFalse(self.map[5, 5].can_pass)
        self.assertTrue(self.map[48, 98].can_pass)
