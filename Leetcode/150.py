from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        import operator
        import math
        ops = { "+": operator.add, "-": operator.sub , "*": operator.mul, "/": operator.truediv} 

        def cal(x, y, op):
            res = ops[op](x, y)
            return math.floor(res) if res >= 0 else math.ceil(res)

        stack = [int(tokens[0]), int(tokens[1])]
        for i in range(2, len(tokens)):
            if tokens[i] in ops:
                y, x = stack.pop(), stack.pop()
                stack.append(cal(x, y, tokens[i]))
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]

