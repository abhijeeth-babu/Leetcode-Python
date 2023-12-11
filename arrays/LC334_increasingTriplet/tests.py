import unittest
from main import Solution

obj = Solution()

class TripletTests(unittest.TestCase):

    def test1(self):
        self.assertEqual(obj.increasingTriplet([1,2,2,1]), False)
    
    
    def test2(self):
        self.assertEqual(obj.increasingTriplet([1,1,1,1]), False)

    def test3(self):
        self.assertEqual(obj.increasingTriplet([2,1,5,0,4,6]), True)


if __name__ == '__main__':
    unittest.main()