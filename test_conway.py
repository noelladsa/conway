import unittest
from conway_board import ConwayBoard


class TDDConway(unittest.TestCase):

    def get_board(self, width, height):
        # return [[random.choice((1, 0) for i in width] for j in height)]
        return [[1, 0, 0],
                [1, 1, 0],
                [1, 0, 1]]

    def setup(self):
        self.w = 3
        self.h = 3
        self.conway_board = ConwayBoard(self.get_board(self.w, self.h),
                                        self.w, self.h)

    def test__get_neighbours_00(self):
        self.setup()
        result = self.conway_board._get_neighbours(0, 0)
        self.assertItemsEqual(result, [(0, 1), (1, 1), (1, 0)])

    def test_get_new_state_00(self):
        self.setup()

        result = self.conway_board._get_next_state(0, 0)
        # This position has atleast two live neighbours
        self.assertEqual(result, 1)

    def test__get_neighbours_01(self):
        self.setup()
        result = self.conway_board._get_neighbours(0, 1)
        self.assertItemsEqual(result, [(0, 0), (1, 1), (1, 0), (1, 2), (0, 2)])

    def test_get_new_state_01(self):
        self.setup()

        result = self.conway_board._get_next_state(0, 1)
        # This position has atleast two neighbours
        self.assertEqual(result, 1)

    def test__get_neighbours_02(self):
        self.setup()
        result = self.conway_board._get_neighbours(0, 2)
        self.assertItemsEqual(result, [(1, 1), (0, 1), (1, 2)])

    def test_get_new_state_02(self):
        self.setup()

        result = self.conway_board._get_next_state(0, 2)
        # This position has atleast two neighbours
        self.assertEqual(result, 0)

    def test_get_next_board(self):
        self.setup()
        result = self.conway_board.get_next_board()
        self.assertItemsEqual(result, [[1, 1, 0], [1, 0, 0], [1, 0, 0]])


if __name__ == "__main__":
    unittest.main()
