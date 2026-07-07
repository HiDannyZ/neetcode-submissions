class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sets will only contain no duplicates
        charSet = set()
        left = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                #remove the left most pointer
                charSet.remove(s[left])
                left += 1
            charSet.add(s[r])
            #get the current size by doing right  - left + 1(+1 bc working with range?)
            res = max(res, r - left + 1)

        return res


        