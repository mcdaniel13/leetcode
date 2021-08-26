from typing import List


class Solution:
    def __init__(self):
        self.dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.max_i = None
        self.max_j = None

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.max_i = len(matrix)
        self.max_j = len(matrix[0])
        dp = [[0] * self.max_j for _ in range(self.max_i)]
        res = 0
        for i in range(self.max_i):
            for j in range(self.max_j):
                res = max(res, self.dfs(matrix, dp, i, j))

        return res

    def dfs(self, matrix: List[List[int]], dp: List[List[int]], i: int, j: int) -> int:
        if dp[i][j] != 0:
            return dp[i][j]
        res = 1
        for k in range(len(self.dir)):
            ni = i + self.dir[k][0]
            nj = j + self.dir[k][1]
            if 0 <= ni < self.max_i and 0 <= nj < self.max_j:
                if matrix[ni][nj] > matrix[i][j]:
                    res = max(res, 1 + self.dfs(matrix, dp, ni, nj))
        dp[i][j] = res
        return res


sol = Solution()
print(sol.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
