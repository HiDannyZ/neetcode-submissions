class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Bottleneck: O(n) because we have to always look through the array
        # Make it into a set

        hashset = set(nums)
        res = 0
        count = 0

        for num in hashset:
            if num-1 not in hashset:
                track = num
                while track in hashset:
                    track +=1
                    count+=1
                res = max(res,count)
                count=0
        return res
            