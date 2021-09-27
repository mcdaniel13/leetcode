from typing import List


class Solution:
    def __init__(self):
        self.letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        res = []
        self.recursive(digits, 0, "", res)
        return res

    def recursive(self, digits, idx, st, res):
        if len(digits) == 0:
            res.append(st)
            return

        digit = int(digits[idx]) - 2
        for ch in self.letters[digit]:
            st += ch
            self.recursive(digits[idx + 1:], idx, st, res)
            st = st[:-1]


sol = Solution()
# print(sol.letterCombinations("23"))
print(sol.letterCombinations(""))
print(sol.letterCombinations("2"))
