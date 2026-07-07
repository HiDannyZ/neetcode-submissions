class Solution:
    def findMin(self, nums: List[int]) -> int:

        #Danny sol has l, r = 0, ....
        start , end = 0, len(nums) - 1 

        res = nums[0]

        while start <= end:
            #base case
            if(nums[start] <= nums[end]):
                res = min(res, nums[start])
                break
            
            #floor divide 
            mid = (start + end)//2
            res = min(res, nums[mid])

            if(nums[mid] >= nums[start]):
                start = mid + 1
            else:
                end = mid - 1
            
        return res


