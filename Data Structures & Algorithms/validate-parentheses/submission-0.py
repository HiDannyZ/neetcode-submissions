class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        order = []
        for i, c in enumerate(s):
            if(c == '(' or c == '[' or c == '{'):
                order.append(c)
            else:
                if len(order) == 0:
                    return False
                popped = order.pop(-1)
                if c == ')' and popped != '(':
                    return False
                elif c == ']' and popped != '[':
                    return False
                elif c == '}' and popped != '{':
                    return False
        if len(order) != 0:
            return False
        return True