from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic = dict()
        for i in range(1, len(nums) + 1):
            dic[i] = 0

        for num in nums:
            dic[num] += 1

        res = []
        for i, v in dic.items():
            if v == 0:
                res.append(i)

        return res


sol = Solution()
print(sol.findDisappearedNumbers([1, 2, 3, 5, 5]))
