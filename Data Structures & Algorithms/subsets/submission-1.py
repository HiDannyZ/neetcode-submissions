class Solution:
    def subsets(self, nums):
        res = []
        subset = []
        self.dfs(nums, 0, subset, res)
        return res

    def dfs(self, nums, i, subset, res):
        if i >= len(nums):
            res.append(subset.copy())
            return

        # Decision to include nums[i]
        subset.append(nums[i])
        self.dfs(nums, i + 1, subset, res)

        # Decision to not include nums[i]
        subset.pop()
        self.dfs(nums, i + 1, subset, res)