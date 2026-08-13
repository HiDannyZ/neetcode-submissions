class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        self.dfs(0,0,[],nums,target,res)
        return res
    

    def dfs(self, index,total,curr, nums, target,res):
        if total == target:
            res.append(curr.copy())
            return
        if index == len(nums) or total > target:
            return
        curr.append(nums[index])
        self.dfs(index, total + nums[index], curr,nums,target, res)
        curr.remove(nums[index])
        self.dfs(index + 1, total, curr,nums,target, res)
