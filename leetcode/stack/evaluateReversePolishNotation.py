class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        validSymbols = "+-*/"
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in validSymbols:
                right, left = stack.pop(), stack.pop()
                if tokens[i] == "+":
                    stack.append(left+right)
                elif tokens[i] == "-":
                    stack.append(left-right)
                elif tokens[i] == "*":
                    stack.append(left*right)
                else:
                    stack.append(int(float(left)/right))
            else:
                stack.append(int(tokens[i]))
                
        return stack.pop()