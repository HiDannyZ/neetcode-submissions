class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        self.dfs(0,digits,digitToChar,[],res)
        return res

    def dfs(self,index,digits,digitToChar,curSet, res):
        if index == len(digits):
            res.append("".join(curSet))  # fixed result formatting
            return
        
        for character in digitToChar[digits[index]]:
            curSet.append(character)
            self.dfs(index + 1, digits, digitToChar, curSet, res)
            curSet.pop()
        