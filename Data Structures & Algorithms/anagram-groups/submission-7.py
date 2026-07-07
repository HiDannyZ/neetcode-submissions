class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagramMap = {}
        for word in strs:
            arraySortedWord = sorted(word)
            sortedWord = "".join(arraySortedWord)
            if sortedWord in anagramMap:
                anagramMap[sortedWord].append(word)
            else:
                anagramMap[sortedWord] = [word]
        for k,v in anagramMap.items():
            res.append(v)
        return res