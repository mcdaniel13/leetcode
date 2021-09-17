from typing import List
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        res = []
        self.recursive(counter, [], res, len(nums))

        return res

    def recursive(self, counter: Counter, arr: List[int], res: List[List[int]], n: int):
        if len(arr) == n:
            res.append(list(arr))
            return
        for key in counter:
            if counter[key] == 0:
                continue
            counter[key] -= 1
            arr.append(key)
            self.recursive(counter, arr, res, n)
            arr.pop(-1)
            counter[key] += 1


sol = Solution()
print(sol.permuteUnique([1, 1, 2]))
print(sol.permuteUnique([1, 2, 3]))
