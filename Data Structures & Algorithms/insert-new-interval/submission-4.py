class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # O(n) time complexity
        # Condition one: When to Merge:
            # Don't append
            # update new Interval
        # Condition two: When to append it into the list
        # Else
            # Append
        res = []
        index = 0
        for i,interval in enumerate(intervals):
            # New Interval id merged in
            index = i
            # Discovered interval cannot be merged
            if interval[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif interval[1] >= newInterval[0]:
                newInterval[0] = min(interval[0],newInterval[0])
                newInterval[1] = max(interval[1],newInterval[1])
            else:
                res.append(interval)
        res.append(newInterval)
        return res


        

