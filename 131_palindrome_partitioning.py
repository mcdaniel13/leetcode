from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.check(s, [], res)
        return res

    def check(self, s: str, sub: List[str], res: List[List[str]]) -> None:
        if s == "":
            new_sub = sub[:]
            res.append(new_sub)
            return

        for i in range(len(s)):
            st = s[:i + 1]
            if st == st[::-1]:
                sub.append(st)
                self.check(s[i + 1:], sub, res)
                sub.pop()

sol = Solution()
print(sol.partition("aab"))
print(sol.partition("a"))
