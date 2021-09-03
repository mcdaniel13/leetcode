from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        hIdx = 0
        while hIdx + 1 <= n * 2:
            vIdx = hIdx
            remain = len(matrix) - hIdx - 1
            while vIdx < remain:
                i = vIdx
                j = hIdx
                val = matrix[i][j]
                for _ in range(4):
                    ni = j
                    nj = n - i - 1
                    matrix[ni][nj], val = val, matrix[ni][nj]
                    i, j = ni, nj
                vIdx += 1
            hIdx += 1


sol = Solution()
# matrix0 = [[1,2,3],[4,5,6],[7,8,9]]
# sol.rotate(matrix0)
# print(matrix0)

matrix1 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
sol.rotate(matrix1)
print(matrix1)

matrix2 = [[1]]
sol.rotate(matrix2)
print(matrix2)

matrix3 = [[1, 2], [3, 4]]
sol.rotate(matrix3)
print(matrix3)
