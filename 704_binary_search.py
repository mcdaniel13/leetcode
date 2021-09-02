from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)

    def binarySearch(self, nums: List[int], start: int, end: int, target: int) -> int:
        if start > end:
            return -1

        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearch(nums, mid + 1, end, target)
        else:
            return self.binarySearch(nums, start, mid - 1, target)


sol = Solution()
print(sol.search([-1, 0, 3, 5, 9, 12], 2))
print(sol.search([-1, 0, 3, 5, 9, 12], 9))
print(sol.search([-1, 0, 3, 5, 9, 12], 2))
