from typing import List


class Solution:
    def generate_next(self, numRows: int, n: int, res: List[List[int]]) -> None:
        if numRows < n:
            return

        li = [1] * n
        for i in range(1, len(li) - 1):
            li[i] = res[-1][i - 1] + res[-1][i]

        res.append(li)
        self.generate_next(numRows, n + 1, res)

    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res

        res = [[1],[1,1]]
        if numRows == 2:
            return res

        n = 3
        self.generate_next(numRows, n, res)
        return res

sol = Solution()
print(sol.generate(5))
print(sol.generate(1))