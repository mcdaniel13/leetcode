from bisect import insort
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        arr = []
        for i in range(len(nums1)):
            insort(arr, [nums1[i] + nums2[0], [i, 0]])

        res = []
        while len(arr) > 0:
            if len(res) == k:
                break
            cord = arr.pop(0)
            i1 = cord[1][0]
            i2 = cord[1][1]
            res.append([nums1[i1], nums2[i2]])
            if i2 < len(nums2) - 1:
                insort(arr, [nums1[i1] + nums2[i2 + 1], [i1, i2 + 1]])
        return res


sol = Solution()
print(sol.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
print(sol.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
print(sol.kSmallestPairs([1, 2], [3], 3))
