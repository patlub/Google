import unittest
from coded_msgs import answer


class CodedMsgsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_wrong_arg_types(self):
        """Sholud raise TypeError for wrong argument types"""
        self.assertRaises(TypeError, answer, 'hello', [])

    def test_non_int_list_items(self):
        """Should return error message"""
        self.assertEqual(answer(['a', 'b'], 12),
                         'All list items should be positive '
                         'integers between 0 and 100')

    def test_negative_list_items(self):
        """Should return error message"""
        self.assertEqual(answer([-2, -6], 12),
                         'All list items should be positive'
                         ' integers between 0 and 100')

    def test_list_items_outside_range(self):
        """Should return error message"""
        self.assertEqual(answer([2, 200], 12),
                         'All list items should be positive '
                         'integers between 0 and 100')

    def test_broadcast_more_than_100_elements(self):
        """Should return error message"""
        my_list = [i for i in range(1, 100)]
        my_list += [1, 3, 4, 8, 9]
        self.assertEqual(answer(my_list, 12),
                         'Broadcast more than 100 elements')

    def test_negative_key(self):
        """Should return error message"""
        self.assertEqual(answer([2, 6], -12),
                         'key should be a positive integer '
                         'between 0 and 250')

    def test_key_out_of_range(self):
        """Should return error message"""
        self.assertEqual(answer([2, 6], 300),
                         'key should be a positive integer '
                         'between 0 and 250')

    def test_list1_with_available_sublist(self):
        """Should return [4, 3, 5] when passed [4, 3, 5, 7, 8] and 12"""
        my_list = [4, 3, 5, 7, 8]
        self.assertEqual(answer(my_list, 12), [0, 2])

    def test_list3_with_available_sublist(self):
        """Should return [2, 3] when passed [4, 3, 10, 2, 8] and 12"""
        my_list = [4, 3, 10, 2, 8]
        self.assertEqual(answer(my_list, 12), [2, 3])

    def test_list4_with_available_sublist(self):
        """Should return [2, 3] when passed [4, 3, 10, 2, 8] and 12"""
        my_list = [i for i in range(1, 11)]
        self.assertEqual(answer(my_list, 21), [0, 5])

    def test_list5_with_available_sublist(self):
        """Should return [2, 3] when passed [4, 3, 10, 2, 8] and 12"""
        my_list = [1, 2, 3]
        self.assertEqual(answer(my_list, 6), [0, 2])

    def test_list6_with_available_sublist(self):
        """Should return [2, 3] when passed [4, 3, 10, 2, 8] and 12"""
        my_list = [10, 2, 3]
        self.assertEqual(answer(my_list, 10), [0, 0])

    def test_list_with_no_match(self):
        """Should return [-1, -1] when passed [1, 2, 3, 4]"""
        my_list = [1, 2, 3, 4]
        self.assertEqual(answer(my_list, 15), [-1, -1])


if __name__ == '__main__':
    unittest.main()
