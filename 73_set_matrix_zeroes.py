from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        flags = [[False] * len(matrix), [False] * len(matrix[0])]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    flags[0][i] = True
                    flags[1][j] = True
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if flags[0][i] is True or flags[1][j] is True:
                    matrix[i][j] = 0


sol = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes(matrix)
print(matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol.setZeroes(matrix)
print(matrix)