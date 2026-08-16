class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        charSet = set()
        length = 0
        for r in range(len(s)):
            theChar = s[r]
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
                length-=1
            charSet.add(s[r])
            length+=1
            res = max(res,length)
        return res


