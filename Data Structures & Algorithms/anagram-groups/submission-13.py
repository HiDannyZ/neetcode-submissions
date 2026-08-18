class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        wordMap = {}
        for word in strs:
            charArray = [0] * 26
            for letter in word:
                charArray[ord(letter) - 97] +=1
            key = tuple(charArray)
            
            if key not in wordMap:
                wordMap[key] = [word]
            else:
                wordMap[key].append(word)
        
        res = []


        return list(wordMap.values())
            
