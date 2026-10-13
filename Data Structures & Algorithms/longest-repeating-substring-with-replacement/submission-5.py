class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Naive Thoughts:
            # Keep track of how many k we use
            # What did we use K on
            # Keep track of the frequencies 
                # HashMap:
        freqCount = {}

        # Sliding window
            # L AND R
                # L 
                    # Moves only when K is going to go below 0
                # R continues and increments the freq
                    # Keep track of the max of the freq in hashmap
                        # Bottle neck of O(N)
        l = 0
        res = 0
        countLen = 0
        for r in range(len(s)):
            
            freqCount[s[r]] = 1 + freqCount.get(s[r],0)
            countLen +=1
            
            
            if r-l + 1 - max(freqCount.values()) > k:
                freqCount[s[l]] -=1
                l+=1
                countLen -=1
            res = max(res,countLen)
        
        return res
                