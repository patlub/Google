import unittest
from dooms_day_fuel import answer


class DoomsDayFuelTestCase(unittest.TestCase):
    def test_arg_type(self):
        """Arg type should be a matrix"""
        self.assertRaises(TypeError, answer, 3)
        self.assertRaises(TypeError, answer, ['a'])

    def test_matrix_out_of_acceptable_range(self):
        """Should return error msg for matrix out of range"""
        self.assertEqual(answer([]),
                         'Matrix elements out of acceptable range(10 X 10)')

    def test_matrix_elements_out_of_acceptable_range(self):
        """Should return error msg for matrix out of range"""
        matrix = [[], [3, 2, 3, 3, 3, 3]]
        self.assertEqual(answer(matrix),
                         'Inner list out of acceptable range(10)')

    def test_matrix_elements_with_non_ints(self):
        """Should return error msg for matrix with non ints in lists"""
        matrix = [[2, 2, 'a', 2, 2, 3], [3, 2, 3, 3, 3, 3]]
        self.assertEqual(answer(matrix),
                         'Matrix should not contain non integers')

    def test_for_negative_list_elements(self):
        """Should return error msg for matrix with negative values"""
        matrix = [[2, 2, -1, 2, 2, 3], [3, 2, 3, 3, 3, 3]]
        self.assertEqual(answer(matrix), 'List should not contain negatives')

    def test_multiple_matrices(self):
        assert (
            answer([
                [0, 2, 1, 0, 0],
                [0, 0, 0, 3, 4],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]) == [7, 6, 8, 21]
        )

        assert (
            answer([
                [0, 1, 0, 0, 0, 1],
                [4, 0, 0, 3, 2, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]
            ]) == [0, 3, 2, 9, 14]
        )

        assert (
            answer([
                [1, 2, 3, 0, 0, 0],
                [4, 5, 6, 0, 0, 0],
                [7, 8, 9, 1, 0, 0],
                [0, 0, 0, 0, 1, 2],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]
            ]) == [1, 2, 3]
        )
        self.assertEqual (
            answer([[0]]), [1, 1])

        assert (
            answer([
                [0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
                [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
                [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
                [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]) == [1, 2, 3, 4, 5, 15]
        )

        self.assertEqual(
            answer([
                [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
                [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
                [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
                [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
                [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]), [4, 5, 5, 4, 2, 20]
        )

        assert (
            answer([
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]) == [1, 1, 1, 1, 1, 5]
        )

        assert (
            answer([
                [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]) == [2, 1, 1, 1, 1, 6]
        )

        assert (
            answer([
                [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
                [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
                [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]) == [6, 44, 4, 11, 22, 13, 100]
        )

        assert (
            answer([
                [0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
                [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
                [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
                [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
                [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]) == [1, 1, 1, 2, 5]
        )


if __name__ == '__main__':
    unittest.main()
