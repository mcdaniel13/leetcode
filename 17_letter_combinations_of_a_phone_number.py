from typing import List


class Solution:
    def __init__(self):
        self.li = ["abc", "def", "ghi",
                   "jkl", "mno", "pqrs",
                   "tuv", "wxyz"]

    def findLetterCombinations(self, res: List[str], digits: str, idx: int, s: str) -> None:
        if idx == len(digits):
            res.append(s)
            return

        digit = int(digits[idx])
        for i in range(len(self.li[digit - 2])):
            s += self.li[digit - 2][i]
            self.findLetterCombinations(res, digits, idx + 1, s)
            s = s[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        self.findLetterCombinations(res, digits, 0, "")
        return res


sol = Solution()
print(sol.letterCombinations("23"))
print(sol.letterCombinations(""))
print(sol.letterCombinations("2"))
