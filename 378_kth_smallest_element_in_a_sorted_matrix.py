from typing import List
from bisect import insort


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                insort(arr, matrix[i][j])

        return arr[k - 1]

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        q = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if len(q) == 0:
                    q.append(matrix[i][j])
                else:
                    self.insert(q, 0, len(q), matrix[i][j])
        return q[k - 1]

    def insert(self, q, l, r, val):
        if l >= r:
            q.insert(l, val)
            return

        mid = (l + r) // 2

        if q[mid] >= val:
            self.insert(q, l, mid, val)
        else:
            self.insert(q, mid + 1, r, val)


sol = Solution()
print(sol.kthSmallest([[1, 2], [1, 3]], 8))
print(sol.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
print(sol.kthSmallest([[-5]], 1))
