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


if __name__ == '__main__':
    unittest.main()
