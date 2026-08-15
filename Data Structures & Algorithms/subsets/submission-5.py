class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Decision tree of options 
        # TC: O(2^n) because there are 2 decisions everytime and the factors never change
        # Backtreking solution
            # We want to explore every single combination
        res = []
        # Populate Res with the answer
        self.dfs(0,[],nums,res)
        return res

    # Function: Get every single combination     
    def dfs(self,index,currArray,nums,res):
        if index == len(nums):
            res.append(currArray.copy())
            return

        val = nums[index]
    
        # We decided to add the val
        currArray.append(val)
        self.dfs(index+1,currArray,nums,res)
        # We decided to not add the val
        currArray.pop()
        self.dfs(index+1,currArray,nums,res)