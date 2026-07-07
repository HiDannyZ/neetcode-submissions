class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countFirstWord = {}
        countSecondWord = {}

        for c in s:
            countFirstWord[c] = countFirstWord.get(c,0) + 1
        for c in t:
            countSecondWord[c] = countSecondWord.get(c,0) + 1
        return countFirstWord == countSecondWord