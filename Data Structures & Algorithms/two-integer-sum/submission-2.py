class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Result: Indices that add up to target
        
        # Key = curNum
        # val = index of curNum
        hashMap = {}
        for i,num in enumerate(nums):
            if target - num in hashMap:
                return [hashMap[target-num], i]
            else:
                hashMap[num] = i
        return False