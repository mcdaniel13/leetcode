import sys
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        minFirst = sys.maxsize
        minSecond = sys.maxsize
        for num in nums:
            minFirst = min(minFirst, num)
            if minFirst < num:
                minSecond = min(num, minSecond)

            if num > minSecond:
                return True

        return False

sol = Solution()
# print(sol.increasingTriplet([1, 2, 3, 4, 5]))
# print(sol.increasingTriplet([5, 4, 3, 2, 1]))
print(sol.increasingTriplet([2, 1, 5, 0, 4, 6]))
