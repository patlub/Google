import unittest
from dont_get_volunteered import answer


class DontGetVolunteeredTestCase(unittest.TestCase):
    def test_moves(self):
        """Should return right number of moves"""
        src = 29
        self.assertEqual(answer(src, 0), 4)
        self.assertEqual(answer(src, 16), 4)
        self.assertEqual(answer(src, 32), 4)
        self.assertEqual(answer(src, 48), 4)
        self.assertEqual(answer(src, 11), 4)
        self.assertEqual(answer(src, 43), 4)
        self.assertEqual(answer(src, 47), 4)
        self.assertEqual(answer(src, 51), 3)
        self.assertEqual(answer(src, 62), 3)
        self.assertEqual(answer(src, 55), 3)
        self.assertEqual(answer(src, 2), 2)
        self.assertEqual(answer(src, 50), 2)
        self.assertEqual(answer(src, 59), 2)
        self.assertEqual(answer(src, 61), 2)
        self.assertEqual(answer(src, 22), 2)
        self.assertEqual(answer(src, 31), 2)
        self.assertEqual(answer(src, 63), 2)
        self.assertEqual(answer(src, 12), 1)
        self.assertEqual(answer(src, 39), 1)
        self.assertEqual(answer(src, 29), 0)
        # self.assertEqual(answer(0, 63), 6)

    def test_arg_type(self):
        """Should raise TypeError"""
        self.assertRaises(TypeError, answer, 2, 'q')
        self.assertRaises(TypeError, answer, 'z', 'q')
        self.assertRaises(TypeError, answer, 'z', 8)

    def test_args_range(self):
        """Should return error message"""
        self.assertEqual(answer(2, 64),
                         'Destination argument out of valid range(0 - 63)')
        self.assertEqual(answer(64, 6),
                         'Source argument out of valid range(0 - 63)')
        self.assertEqual(answer(64, 66),
                         'Source argument out of valid range(0 - 63)')


if __name__ == '__main__':
    unittest.main()
