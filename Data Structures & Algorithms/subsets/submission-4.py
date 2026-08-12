class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Is nums possible to be empty
        # Can I get duplicate numbers
        # are the nums sorted

        # BottleNeck: nlogn
        nums.sort()

        res = []
        self.dfs(0,[],nums,res)

        return res

        
    


    # Stack implementation
    # TC: O(nlogn) 
    def dfs(self,index, current, nums, res):
        # Base Case
        if index == len(nums):
            res.append(current.copy())
            return

        current.append(nums[index])
        self.dfs(index+1,current,nums,res)
        
        current.remove(nums[index])
        self.dfs(index+1,current,nums,res)