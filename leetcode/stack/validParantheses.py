class Solution:
    def isValid(self, s: str) -> bool:
        symbols = {'(':')', '{': '}', '[':']'}
        stack = []
        for x in s:
            if x in symbols.keys():
                stack.append(symbols[x])
            elif x in symbols.values():
                try:
                    value = stack.pop()
                    if x != value:
                        return False
                except:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        return False
    