# Given an array of meeting time intervals consisting of start and end
# times [[s1,e1], [s2,e2],...], find the minimum number of conference
# rooms required.

# Example1
#     Input: intervals = [(0,30),(5,10),(15,20)]
#     Output: 2
#     Explanation:
#     We need two meeting rooms
#     room1: (0,30)
#     room2: (5,10),(15,20)

# Example2
#     Input: intervals = [(2,7)]
#     Output: 1
#     Explanation:
#     Only need one meeting room

import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s, e = 0, 0
        rooms, res = 0, 0

        while s < len(start):
            if start[s] < end[e]:
                rooms += 1
                res = max(res, rooms)
                s += 1
            else:
                e += 1
                rooms -= 1

        return res