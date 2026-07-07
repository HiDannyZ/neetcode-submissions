class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        length = len(intervals)
        
        index = 0


        # Step 1: Add all intervals before newInterval starts
        # [1,2][5,10][11,15],    newInterval = [6,12]
        # Comparing endValue of newInterval
        while index < length and newInterval[0] > intervals[index][1]:
            res.append(intervals[index]) 
            index+=1
        
        #Perform Merging
        while index < length and newInterval[1] >= intervals[index][0]:
            newInterval[0] = min(newInterval[0],intervals[index][0])
            newInterval[1] = max(newInterval[1],intervals[index][1])
            index+=1
        res.append(newInterval)

        while index < length:
            res.append(intervals[index])
            index+=1


        return res
        