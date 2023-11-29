import unittest
from main import Solution

obj = Solution()

class TestPermutations(unittest.TestCase):

    def test_example_1(self):
        nums = [1, 2, 3]
        expected_output = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(sorted(obj.permute(nums)), sorted(expected_output))

    def test_example_2(self):
        nums = [0, 1]
        expected_output = [[0, 1], [1, 0]]
        self.assertEqual(sorted(obj.permute(nums)), sorted(expected_output))

    def test_example_3(self):
        nums = [1]
        expected_output = [[1]]
        self.assertEqual(sorted(obj.permute(nums)), sorted(expected_output))


if __name__ == '__main__':
    unittest.main()
