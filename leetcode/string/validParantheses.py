#https://leetcode.com/problems/valid-parentheses/
# o(n) time complexity o(n) space complexity
def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {'{': '}',  '[': ']', '(': ')'}
        for x in s:

            if x in dic.keys():
                stack.append(dic[x])

            elif x in dic.values():
                try:
                    value = stack.pop()
                    if value != x:
                        return False
                except:
                    return False
                
            else:
                return False
            
            
        if len(stack) == 0:
            return True
        return False
        