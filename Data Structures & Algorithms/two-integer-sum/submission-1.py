class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Key = target - num
        # Value = index
        hashmap = {}

        for index in range(len(nums)):
            if nums[index] in hashmap:
               return [hashmap[nums[index]], index]
            else:
                hashmap[target-nums[index]] = index
                

