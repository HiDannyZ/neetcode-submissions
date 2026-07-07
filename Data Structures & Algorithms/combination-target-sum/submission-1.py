class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs([],res,0, nums,0,target)
        return res
    
    def dfs(self,curArray,res,index, nums, total, target):
        if total > target or index >= len(nums):
            return
        if total == target:
            res.append(curArray.copy())
            return
        curArray.append(nums[index])
        self.dfs(curArray, res, index, nums, total+nums[index],target)
        curArray.pop()
        self.dfs(curArray, res, index+1, nums, total,target)
       #  