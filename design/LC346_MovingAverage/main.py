# Given a stream of integers and a window size, calculate the moving
# average of all integers in the sliding window.

# MovingAverage m = new MovingAverage(3)
# m.next(1) = (1) --> 1
# m.next(10) = (10 + 1) --> 5.5
# m.next(3) = (3 + 10 + 1) --> 4.66667
# m.next(5) = (5 + 3 + 10) --> 6

# use q for O(1) in and out ops
from collections import deque
class MovingAverage:

    def __init__(self, size):
        self.window = deque()
        self.size = size
        self.sum = 0


    def next(self, val):
        if len(self.window) == self.size:
            self.sum -= self.window.popleft()
        self.window.append(val)
        self.sum += val
        return self.sum / len(self.window)
    

