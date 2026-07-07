class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(1) in obtaining values and insertings
        hashmap = {}

        for i in range(len(nums)):
            if target-nums[i] in hashmap:
                return [hashmap[target-nums[i]],i]
            hashmap[nums[i]] = i
        