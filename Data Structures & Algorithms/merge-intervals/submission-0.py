class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Key Points: Array is not sorted in anyway
        # Naive solution Sorting it by the start times of each interval
        # Check if l and r pointer

        # If end of initial > start of next

        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
            