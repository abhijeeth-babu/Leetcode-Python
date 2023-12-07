from main import Solution
import unittest

class TestGCDofStrings(unittest.TestCase):

    def test_example1(self):
        str1 = "ABCABC"
        str2 = "ABC"
        expected_result = "ABC"
        actual_result = Solution().gcdOfStrings(str1, str2)
        self.assertEqual(expected_result, actual_result)

    def test_example2(self):
        str1 = "ABABAB"
        str2 = "ABAB"
        expected_result = "AB"
        actual_result = Solution().gcdOfStrings(str1, str2)
        self.assertEqual(expected_result, actual_result)

    def test_example3(self):
        str1 = "LEET"
        str2 = "CODE"
        expected_result = ""
        actual_result = Solution().gcdOfStrings(str1, str2)
        self.assertEqual(expected_result, actual_result)

    def test_empty_string(self):
        str1 = ""
        str2 = "ABC"
        expected_result = ""
        actual_result = Solution().gcdOfStrings(str1, str2)
        self.assertEqual(expected_result, actual_result)

    def test_different_lengths(self):
        str1 = "ABCD"
        str2 = "ABC"
        expected_result = ""
        actual_result = Solution().gcdOfStrings(str1, str2)
        self.assertEqual(expected_result, actual_result)

    def test_no_common_divisor(self):
        str1 = "ABACABA"
        str2 = "CABA"
        expected_result = ""
        actual_result = Solution().gcdOfStrings(str1, str2)
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()