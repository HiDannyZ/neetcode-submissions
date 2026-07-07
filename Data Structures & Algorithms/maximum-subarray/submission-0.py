class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Negative: We reset
        # Bottleneck: O(n) to go through the whole array
        if not nums:
            return 
        res,curMax = nums[0], nums[0]
        for index in range(1,len(nums)):
            if curMax < 0:
                curMax = 0
            curMax+= nums[index]
            res = max(res,curMax)
        return res
            
            