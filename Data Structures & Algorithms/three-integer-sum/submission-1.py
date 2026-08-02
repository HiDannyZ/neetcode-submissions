class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Is nums Sorted? - No
        # Can we return empty []? - Yes
        res = []

        # Lets Sort the Array to make distinct property easier
        # TC - O(nlogn)
        nums.sort()


        # Naive computation TC - O(n^3)
        # Optimized computation TC - O(n^2)
        # a - be our pivot point
        # b and c will be our window

        for i,a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            b = i + 1
            c = len(nums)-1
            while b < c:
                total = a + nums[b] + nums[c]
                if total == 0:
                    res.append([a,nums[b],nums[c]])
                    b+=1
                    c-=1
                    while (b < c) and nums[b] == nums[b-1]:
                        b += 1
                elif total > 0:
                    c-=1
                else:
                    b+=1
        # [-4,-1,-1, 0 , 1,2,]
        #   a  b           c




        return res