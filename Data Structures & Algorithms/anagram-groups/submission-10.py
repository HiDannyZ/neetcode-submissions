class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []
        for word in strs:
            sortedWord = sorted(word)
            sortedStringWord = "".join(sortedWord)
            if sortedStringWord in hashmap:
                hashmap[sortedStringWord].append(word)
            else:
                hashmap[sortedStringWord] = [word]
        
        for val in hashmap.values():
            res.append(val)
        return res
