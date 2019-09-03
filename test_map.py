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

    def test_nodes_connection(self):
        self.map = Map((100, 100))
        self.assertEqual((42, 54), self.map[43, 54].left.loc)
        self.assertEqual((44, 54), self.map[43, 54].right.loc)
        self.assertEqual((43, 53), self.map[43, 54].up.loc)
        self.assertEqual((43, 55), self.map[43, 54].down.loc)
        self.assertEqual((42, 53), self.map[43, 54].lu.loc)
        self.assertEqual((44, 53), self.map[43, 54].ru.loc)
        self.assertEqual((42, 55), self.map[43, 54].ld.loc)
        self.assertEqual((44, 55), self.map[43, 54].rd.loc)
        self.assertEqual((1, 0), self.map[0, 0].right.loc)
        self.assertEqual((0, 1), self.map[0, 0].down.loc)
        self.assertEqual((1, 1), self.map[0, 0].rd.loc)
        self.assertIsNone(self.map[0, 0].up)
        self.assertIsNone(self.map[0, 0].left)
        self.assertIsNone(self.map[0, 0].lu)
        self.assertIsNone(self.map[0, 0].ru)
        self.assertIsNone(self.map[0, 0].ld)
