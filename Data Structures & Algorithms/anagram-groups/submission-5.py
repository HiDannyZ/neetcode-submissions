class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list) # for edge case

        for s in strs:
            count = [0] * 26 # a - z (need this for each word to count)

            for char in s:
                # ord("some letter") gets ascii value so
                count[ord(char) - ord('a')] += 1
            
            #tuple bc cannot have lists as keys in python
            sol[tuple(count)].append(s)
        
        # return only the values not keys
        return sol.values()
        