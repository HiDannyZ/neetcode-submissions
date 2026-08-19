class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        badParentheses = set()
        res = []

        # Idea
        # - One pass to Find all indexes of bad parntheses in the list
        # - Another pass to add to res
        for i,letter in enumerate(s):
            if letter == "(":
                stk.append(i)
            else:
                if not stk and letter == ")":
                    badParentheses.add(i)
                if stk and letter == ")":
                    stk.pop()

        while stk:
            badParentheses.add(stk.pop())
        
        for i,letter in enumerate(s):
            if i not in badParentheses:
                res.append(letter)
        return "".join(res)