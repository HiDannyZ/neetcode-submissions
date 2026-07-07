class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        total = 0
        self.dfs(0,subset,total, target, nums, res)
        return res

        
    def dfs(self, i , subset, total, target,nums, res):
        if total > target or i>=len(nums):
            return
        if total == target:
            res.append(subset.copy())
            return
            
        subset.append(nums[i])
        self.dfs(i , subset, total + nums[i], target,nums, res)
        subset.pop()
        self.dfs(i +1 , subset, total, target,nums, res)

