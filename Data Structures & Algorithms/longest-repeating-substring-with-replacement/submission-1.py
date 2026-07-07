class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        res = 0

        #use range for indices 
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            #if the window size - highest count > k /// then it is invalid and we need to update bc too many replacements

            if (r -  left + 1) - (max(count.values())) > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, r - left + 1)
        return res

        