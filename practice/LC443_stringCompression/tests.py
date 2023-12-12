import unittest
from main import Solution

obj = Solution()

class Compress_Test(unittest.TestCase):

    def testcase1(self):
        chars = ["a","a","b","b","c","c","c"]  
        res = obj.compress(chars) 
        self.assertEqual(chars[:res], ["a","2","b","2","c","3"])

    def testcase2(self):
        chars = ["a","a", "a","b","b","c","c","c"]  
        res = obj.compress(chars) 
        self.assertEqual(chars[:res], ["a","3","b","2","c","3"])

    def testcase3(self):
        chars = ["a"]
        res = obj.compress(chars)
        self.assertEqual(chars[:res], ["a"])


if __name__ == '__main__':
    unittest.main()