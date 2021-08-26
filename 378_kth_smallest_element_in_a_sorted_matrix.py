from typing import List
from bisect import insort


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                insort(arr, matrix[i][j])

        return arr[k - 1]


sol = Solution()
print(sol.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
print(sol.kthSmallest([[-5]], 1))
