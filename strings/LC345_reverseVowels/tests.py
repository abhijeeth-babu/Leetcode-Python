import unittest
from main import Solution

obj = Solution()

class reverse_vowels_test(unittest.TestCase):

    def test1(self):
        self.assertEqual(obj.reverseVowels("hello"), "holle")

    def test2(self):
        self.assertEqual(obj.reverseVowels("aA"), "Aa")

    def test3(self):
        self.assertEqual(obj.reverseVowels("leetcode"), "leotcede")


if __name__ == '__main__':
    unittest.main()