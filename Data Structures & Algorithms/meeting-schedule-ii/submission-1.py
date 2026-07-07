"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Line Sweep Algorthim
        events = []

        for i in intervals:
            events.append((i.start,1))
            events.append((i.end,-1))
        
        events.sort()

        active = 0
        res = 0

        for time,delta in events:
            active +=delta
            res = max(res,active)
        return res


