class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxArea = 0

        while r > l:
            area = min(heights[l],heights[r]) * (r-l)
            maxArea = max(maxArea, area)
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return maxArea