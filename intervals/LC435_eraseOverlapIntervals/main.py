class Solution:
    def eraseOverlapIntervals(self, intervals):
        count = 0
        if not intervals:
            return count
        intervals = sorted(intervals, key=lambda x: x[0])

        previous_end = intervals[0][1]

        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            if curr_start < previous_end:
                count += 1
                previous_end = min(curr_end, previous_end)
            else:
                previous_end = curr_end

        return count
            

            
            
            