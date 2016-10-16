import unittest
from twenty48 import Board_2048

class PieceTests(unittest.TestCase):

    def test_single_tile_left(self):
        b = Board_2048([[0, 0, 0],
                        [0, 2, 0],
                        [0, 0, 0]])
        b, motions = b.move_left()
        self.assertEqual(b.rows, [[0, 0, 0],
                                  [2, 0, 0],
                                  [0, 0, 0]])
        self.assertEqual(motions, {(1,1, 1,0)})

    def test_single_tile_left_without_moving(self):
        b = Board_2048([[0, 0, 0],
                        [2, 0, 0],
                        [0, 0, 0]])
        b, motions = b.move_left()
        self.assertEqual(b.rows, [[0, 0, 0],
                                  [2, 0, 0],
                                  [0, 0, 0]])
        self.assertEqual(motions, set())

    def test_two_tiles_up_without_touching(self):
        b = Board_2048([[0, 0, 0],
                        [2, 0, 2],
                        [0, 0, 0]])
        b, motions = b.move_up()
        self.assertEqual(b.rows, [[2, 0, 2],
                                  [0, 0, 0],
                                  [0, 0, 0]])
        self.assertEqual(motions, {(1,0, 0,0), (1,2, 0,2)})

    def test_two_tiles_down_without_combining(self):
        b = Board_2048([[0, 0, 4],
                        [0, 0, 2],
                        [0, 0, 0]])
        b, motions = b.move_down()
        self.assertEqual(b.rows, [[0, 0, 0],
                                  [0, 0, 4],
                                  [0, 0, 2]])
        self.assertEqual(motions, {(0,2, 1,2), (1,2, 2,2)})

    def test_two_tiles_right_combining(self):
        b = Board_2048([[0, 0, 0],
                        [4, 0, 4],
                        [0, 0, 0]])
        b, motions = b.move_right()
        self.assertEqual(b.rows, [[0, 0, 0],
                                  [0, 0, 8],
                                  [0, 0, 0]])
        self.assertEqual(motions, {(1,0, 1,2)})
