from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hidx = 0
        while (hidx + 1) * 2 <= len(matrix):
            vidx = hidx
            vlen = len(matrix) - hidx
            while vidx + 1 < vlen:
                i = hidx
                j = vidx
                val = matrix[i][j]
                for rnd in range(4):
                    temp = matrix[j][len(matrix) - i - 1]
                    matrix[j][len(matrix) - i - 1] = val
                    val = temp
                    i, j = j, len(matrix) - i - 1
                vidx += 1
            hidx += 1
            print(matrix)


sol = Solution()
# matrix0 = [[1,2,3],[4,5,6],[7,8,9]]
# sol.rotate(matrix0)
# print(matrix0)

matrix1 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol.rotate(matrix1)
print(matrix1)

matrix2 = [[1]]
sol.rotate(matrix2)
print(matrix2)

matrix3 = [[1,2],[3,4]]
sol.rotate(matrix3)
print(matrix3)
