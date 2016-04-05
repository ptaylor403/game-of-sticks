import unittest
from game_of_sticks import *

class TestGameOfSticks(unittest.TestCase):
    def test_assert_equal_stick_count(self):
        self.assertEqual(stick_count(10, 3), 7)

    def test_assert_true_is_end(self):
        self.assertTrue(is_end(2, 2))

    def test_assert_false_is_end(self):
        self.assertFalse(is_end(2, 3))



if __name__ == '__main__':
    unittest.main()
