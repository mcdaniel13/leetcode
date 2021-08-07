from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [i for i in range(len(nums) + 1)]
        for num in nums:
            arr[num] *= -1

        arr.sort()
        return arr[-1]


sol = Solution()
print(sol.missingNumber([3, 0, 1]))
print(sol.missingNumber([0, 1]))
print(sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(sol.missingNumber([0]))
