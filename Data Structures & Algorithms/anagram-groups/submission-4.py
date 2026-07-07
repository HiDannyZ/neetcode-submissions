class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Transform the word to alphabetical order to sort them
        # Immutable Key = Sorted String
        # Value = List of words
        # [a,c,t]
        hashMap = {}
        for s in strs:
            sortedWord = ''.join(sorted(s))
            if sortedWord not in hashMap:
                hashMap[sortedWord] = []
            hashMap[sortedWord].append(s)
        res = []
        for key,val in hashMap.items():
            res.append(val) 
            
        return res