import unittest
from lucky_triples import answer


class LuckyTriplesCase(unittest.TestCase):
    def test_arg_type(self):
        """Should raise TypeError for wrong arg type"""
        self.assertRaises(TypeError, answer, 2)

    def test_arg_list_length_is_valid(self):
        """
        Should return error message if arg list length is
        not between 2 and 2000 inclusive 
        """
        self.assertEqual(answer([i for i in range(0, 2001)]),
                         'Arg list length is out of acceptable range')
        self.assertEqual(answer([i for i in range(0, 1)]),
                         'Arg list length is out of acceptable range')

    def test_arg_list_element_type(self):
        """
        Should return error msg if any of the 
        list elements is not an int
        """
        self.assertEqual(answer(['q', 't']),
                         'Arg list contains elements outside acceptable range')

    def test_arg_list_elements_are_in_valid_range(self):
        """
        Should return error msg if arg list elements
        are not between 1 and 999999 inclusive
        """
        l = [1, 1000000]
        self.assertEqual(answer(l),
                         'Arg list contains elements outside acceptable range')


if __name__ == '__main__':
    unittest.main()
