class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # We have to sort the intervals. Otherwise, it's extremely difficult. 
        # TC: O(nlogn)   
        intervals.sort(key = lambda x : x[0])

        res = []
        prevInterval = intervals[0]
        for interval in intervals[1:]:
            if prevInterval[1] >= interval[0]:
                prevInterval[0] = min(prevInterval[0],interval[0])
                prevInterval[1] = max(prevInterval[1],interval[1])
            else:
                res.append(prevInterval)
                prevInterval = interval
        res.append(prevInterval)
        return res
            # Base condition
