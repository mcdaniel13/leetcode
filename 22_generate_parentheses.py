from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.recursive(n, "", 0, 0, res)
        return res

    def recursive(self, n: int, s: str, op: int, cl: int, res: List[str]):
        if len(s) == n * 2:
            res.append(s)
            return

        if op < n:
            s += "("
            self.recursive(n, s, op + 1, cl, res)
            s = s[:-1]

        if op > cl:
            s += ")"
            self.recursive(n, s, op, cl + 1, res)
            s = s[:-1]


sol = Solution()
print(sol.generateParenthesis(3))
print(sol.generateParenthesis(5))
print(sol.generateParenthesis(1))
