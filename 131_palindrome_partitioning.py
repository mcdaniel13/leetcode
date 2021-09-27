from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.recursive(s, [], res)
        return res

    def recursive(self, s: str, arr: List[str], res: List[List[str]]):
        if len(s) == 0:
            res.append(list(arr))
            return

        for i in range(len(s)):
            st = s[:i + 1]
            if st == st[::-1]:
                arr.append(st)
                self.recursive(s[i + 1:], arr, res)
                arr.pop(-1)


sol = Solution()
print(sol.partition("aab"))
print(sol.partition("a"))
