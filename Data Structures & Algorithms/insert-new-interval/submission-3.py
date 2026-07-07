class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Qualities to merge
        '''
            if newInterval start is less than interval end  
            if newInterval end is equal to or > start of interval
        '''

        # Qualities to not merge
        '''
            if newInterval start is > interval End -- If newInterval comes after the current interval (i.e., newInterval[0] > intervals[index][1]
            
            if newInterval end is < interval Start -- If newInterval comes before
        '''

        res = []
        index = 0
        length = len(intervals)
        # Find when we need to merge aka when newInterval is within one of the intervals
        while index < length and (newInterval[0] > intervals[index][1]) :    
            res.append(intervals[index])
            index+=1

        # Proceed to Merge

        while index < length and (newInterval[0] <= intervals[index][1] and newInterval[1] >= intervals[index][0]):
            start = min(newInterval[0], intervals[index][0])
            end = max(newInterval[1],intervals[index][1])
            newInterval = [start,end]
            index+=1
        
        res.append(newInterval)

        while index < length:
            res.append(intervals[index])
            index+=1
        return res


    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for index in range(len(intervals)):
            start = intervals[index][0]
            end = intervals[index][1]
            if newInterval[0] > end:
                res.append(intervals[index])
            elif newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[index:]
            else:
                newInterval = [min(newInterval[0],start), max(newInterval[1],end)]
        # This is in case its at the end
        res.append(newInterval)

        return res