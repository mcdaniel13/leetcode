import sys

from typing import List
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dic = defaultdict(set)
        point_dic = defaultdict(int)
        for point in points:
            if (point[0], point[1]) in point_dic.keys():
                point_dic[(point[0], point[1])] += 1
            else:
                point_dic[(point[0], point[1])] = 1

        duplicates = []
        for key, value in point_dic.items():
            duplicates.append([key[0], key[1], value])

        for i in range(len(duplicates) - 1):
            for j in range(i + 1, len(duplicates)):
                po1 = points[i]
                po2 = points[j]
                if po1[0] - po2[0] == 0:
                    slope = sys.maxsize
                else:
                    slope = (po1[1] - po2[1]) / (po1[0] - po2[0])
                remain = po1[1] - slope * po1[0]
                dic[(slope, remain)].add(i)
                dic[(slope, remain)].add(j)

        res = 1
        for key, values in dic.items():
            sum = 0
            for value in values:
                sum += duplicates[value][2]
            res = max(sum, res)
        return res


sol = Solution()
print(sol.maxPoints([[4, 5], [4, -1], [4, 0]]))
print(sol.maxPoints([[1, 1], [2, 2], [3, 3]]))
print(sol.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
