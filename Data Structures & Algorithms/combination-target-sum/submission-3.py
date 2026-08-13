class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        self.dfs(0,0,[],nums,target,res)
        return res
    

    def dfs(self, index,total,currArray, nums, target,res):
        if total == target:
            res.append(currArray.copy())
            return
        if index == len(nums) or total > target:
            return
        val = nums[index]
        currArray.append(val)
        self.dfs(index, total + val, currArray,nums,target, res)
        currArray.remove(val)
        self.dfs(index + 1, total, currArray,nums,target, res)
