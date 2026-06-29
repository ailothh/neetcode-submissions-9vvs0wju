"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start)
        for interval in range(1,len(intervals)):
            i1=intervals[interval-1]
            i2=intervals[interval]
            if i2.start<i1.end:
                return False
        return True