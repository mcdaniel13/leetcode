from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = [0]
        arr = []
        i = 0
        j = 0
        iRange = [1, len(matrix) - 1]
        jRange = [0, len(matrix[0]) - 1]

        arr.append(matrix[0][0])
        while len(arr) < len(matrix) * len(matrix[0]):
            if direction[0] == 0 and j == jRange[1]:
                jRange[1] -= 1
                direction[0] = 2
            elif direction[0] == 1 and j == jRange[0]:
                jRange[0] += 1
                direction[0] = 3
            elif direction[0] == 2 and i == iRange[1]:
                iRange[1] -= 1
                direction[0] = 1
            elif direction[0] == 3 and i == iRange[0]:
                iRange[0] += 1
                direction[0] = 0

            if direction[0] == 0:
                j += 1
            elif direction[0] == 1:
                j -= 1
            elif direction[0] == 2:
                i += 1
            else:
                i -= 1
            arr.append(matrix[i][j])

        return arr

sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))