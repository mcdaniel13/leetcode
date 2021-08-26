from typing import List


class Solution:
    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    def missingNumber(self, nums: List[int]) -> int:
        arr = [i for i in range(len(nums) + 1)]
        for num in nums:
            arr[num] *= -1

        arr.sort()
        return arr[-1]

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def missingNumber2(self, nums: List[int]) -> int:
        sum = 0
        total = 0
        for i in range(len(nums)):
            sum += nums[i]
            total += i + 1
        return total - sum


sol = Solution()
print(sol.missingNumber([3, 0, 1]))
print(sol.missingNumber([0, 1]))
print(sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(sol.missingNumber([0]))
