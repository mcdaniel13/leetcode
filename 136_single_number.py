from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = dict()
        for num in nums:
            if num in dic.keys():
                dic[num] += 1
            else:
                dic[num] = 1

        for key, value in dic.items():
            if value == 1:
                return key

        return -1


sol = Solution()
print(sol.singleNumber([2, 2, 1]))
print(sol.singleNumber([4, 1, 2, 1, 2]))
