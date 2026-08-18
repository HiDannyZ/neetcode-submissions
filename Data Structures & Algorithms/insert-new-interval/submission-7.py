class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        
        
        for i,interval in enumerate(intervals):
            start = interval[0]
            end = interval[1]
            newIntervalStart = newInterval[0]
            newIntervalEnd = newInterval[1]
            if start > newIntervalEnd:
                res.append(newInterval)
                return res + intervals[i:]
            elif end >= newIntervalStart:
                newInterval[0] = min(start,newIntervalStart)
                newInterval[1] = max(end,newIntervalEnd)
            else:
                res.append(interval)
        
        res.append(newInterval)

        return res
