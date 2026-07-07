class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Determine which is the longest string
        #Have a Data structure for storing
        # Bottleneck : We will have to do at least a 1pass
        # O(n)
        
        freqMap = {}
        l = 0
        currMax = 0
        # "AAABABB" k = 1
        #{A:1}       
        #

        for r in range(len(s)):
            # Add Value to HashMap
            freqMap[s[r]] = freqMap.get(s[r],0) + 1


            # Check if substring is valid
            if r-l + 1 - max(freqMap.values()) > k:
                freqMap[s[l]] -=1
                l+=1

            currMax = max(currMax,r-l + 1)
        return currMax

