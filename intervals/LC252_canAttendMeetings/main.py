# Given an array of meeting time intervals consisting of start and end
# times [s1, e1], [s2, e2], ... , determine if a person could attend
#  all meetings.
# ---------------------------
# canAttendMeetings([[0, 30], [5, 10], [15, 20]]) --> False
# canAttendMeetings([[2, 4], [7, 10]]) --> True


class Solution:
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key=lambda x: [x[0], x[1]])
        for i in range(1, len(intervals)):
            prev_meeting_end = intervals[i-1][-1]
            curr_meeting_start = intervals[i][0]
            if prev_meeting_end > curr_meeting_start:
                return False
        
        return True