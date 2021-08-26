from typing import List
from collections import OrderedDict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = dict()
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 0
        res = []
        for key, v in sorted(dic.items(), key=lambda item: item[1], reverse=True):
            res.append(key)
            if len(res) == k:
                break

        return res


sol = Solution()
print(sol.topKFrequent([3, 1, 1, 1, 2, 2], 2))
print(sol.topKFrequent([1], 1))
