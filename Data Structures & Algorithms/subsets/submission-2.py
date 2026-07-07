class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(0,nums,[],res)
        return res


    def dfs(self,index, nums,currArray,res):
        if index == len(nums):
            res.append(currArray.copy())
            return
        currArray.append(nums[index])
        self.dfs(index+1,nums,currArray,res)
        currArray.pop()
        self.dfs(index+1,nums,currArray,res)



