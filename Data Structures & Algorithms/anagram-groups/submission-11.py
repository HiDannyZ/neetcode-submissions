class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordFreq = {}
        res = []

        for word in strs:
            sortedWord = sorted(word)
            sortedStringWord = "".join(sortedWord)
            if sortedStringWord not in wordFreq:
                wordFreq[sortedStringWord] = [word]
            else:
                wordFreq[sortedStringWord].append(word)
                        
        for val in wordFreq.values():
            res.append(val)
        return res

