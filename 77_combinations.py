from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.recursive(n, k, 1, 0, [], res)
        return res

    def recursive(self, n: int, k: int, cur: int, step: int, arr: List[int], res: List[List[int]]):
        if step == k:
            res.append(list(arr))
            return

        for i in range(cur, n + 1):
            arr.append(i)
            self.recursive(n, k, i + 1, step + 1, arr, res)
            arr.pop(-1)


sol = Solution()
print(sol.combine(4, 2))
print(sol.combine(1, 1))
