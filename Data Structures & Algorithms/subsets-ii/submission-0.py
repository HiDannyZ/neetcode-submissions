class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        self.dfs(0,nums,subset,res)
        return res


    def dfs(self,index, nums,subset,res):
        if index == len(nums):
            res.append(subset.copy())
            return
        subset.append(nums[index])
        self.dfs(index+1,nums,subset,res)
        subset.pop()
        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index +=1
        self.dfs(index + 1, nums,subset,res)