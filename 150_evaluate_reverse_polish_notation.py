from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []
        for s in tokens:
            if s == '/':
                i1 = stack.pop()
                i2 = stack.pop()
                stack.append(int(i2 / i1))
            elif s == '*':
                i1 = stack.pop()
                i2 = stack.pop()
                stack.append(i2 * i1)
            elif s == '+':
                i1 = stack.pop()
                i2 = stack.pop()
                stack.append(i2 + i1)
            elif s == '-':
                i1 = stack.pop()
                i2 = stack.pop()
                stack.append(i2 - i1)
            else:
                i = int(s)
                stack.append(i)

        return stack[-1]


sol = Solution()
print(sol.evalRPN(["2", "1", "+", "3", "*"]))
print(sol.evalRPN(["4", "13", "5", "/", "+"]))
print(sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
