from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        self.dfs(s, 0, s, res)
        return res

    def dfs(self, s: str, idx: int, t: str, res: List[str]) -> None:
        if idx == len(s):
            res.append(t)
            return

        if not s[idx].isnumeric():
            if s[idx].isupper():
                ch = s[idx].lower()
            else:
                ch = s[idx].upper()
            self.dfs(s, idx + 1, t[:idx] + ch + t[idx+1:], res)
        self.dfs(s, idx + 1, t, res)


sol = Solution()
print(sol.letterCasePermutation("a1b2"))
print(sol.letterCasePermutation("3z4"))
print(sol.letterCasePermutation("12345"))
print(sol.letterCasePermutation("0"))
