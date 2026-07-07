class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Method 2: charArray [0] * 26
        # Ascii value : ord(char) - ord("a")
        # a -> 26-26
        # 28-26
        # BigO O(n)
        # Space: O(n)

        # Key = tuple of charArray
        # value = list
        anagramMap = defaultdict(list)

        for word in strs:
            charArray = [0] * 26
            for letter in word:
                placement = ord(letter)-ord('a')
                charArray[placement] += 1
            anagramMap[tuple(charArray)].append(word)
        return list(anagramMap.values())

