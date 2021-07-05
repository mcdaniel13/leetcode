from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        li = []
        self.generateParenthesisString(li, "", 0, 0, n)
        return li

    def generateParenthesisString(self, li: List[str], s: str, open: int, close: int, n: int):
        if len(s) == 2 * n:
            li.append(s)
            return
        else:
            if open < n:
                s += "("
                self.generateParenthesisString(li, s, open + 1, close, n)
                s = s[:-1]
            if open > close:
                s += ")"
                self.generateParenthesisString(li, s, open, close + 1, n)

sol = Solution()
print(sol.generateParenthesis(5))
print(sol.generateParenthesis(1))