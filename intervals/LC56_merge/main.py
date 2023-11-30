class Solution:
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        
        return res