from typing import List


class Solution:
    def __init__(self):
        self.inc = [[0, 1], [1, 0]]
        self.dec = [[0, -1], [-1, 0]]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.dfs(matrix, target, 0, 0)

    def dfs(self, matrix: List[List[int]], target: int, i: int, j: int):
        val = matrix[i][j]
        matrix[i][j] = False
        if val < target:
            for ni in self.inc:
                if 0 <= i + ni[0] < len(matrix) and 0 <= j + ni[1] < len(matrix[0]) and matrix[i + ni[0]][j + ni[1]] is not False:
                    if self.dfs(matrix, target, i + ni[0], j + ni[1]):
                        return True
        elif val > target:
            for ni in self.dec:
                if 0 <= i + ni[0] < len(matrix) and 0 <= j + ni[1] < len(matrix[0]) and matrix[i + ni[0]][j + ni[1]] is not False:
                    if self.dfs(matrix, target, i + ni[0], j + ni[1]):
                        return True
        else:
            return True

        return False


sol = Solution()
print(sol.searchMatrix(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
print(sol.searchMatrix(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20))
