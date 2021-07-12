from typing import List


class Solution:
    def partition(self, nums: List[int], start: int, end: int) -> int:
        pivotIndex = start
        pivot = nums[start]

        while start < end:
            while start < len(nums) and nums[start] <= pivot:
                start += 1
            while nums[end] > pivot:
                end -= 1

            if start < end:
                nums[start], nums[end] = nums[end], nums[start]

        nums[end], nums[pivotIndex] = nums[pivotIndex], nums[end]

        return end

    def quickSort(self, nums: List[int], start: int, end: int) -> None:
        if start < end:
            pivot = self.partition(nums, start, end)
            self.quickSort(nums, start, pivot - 1)
            self.quickSort(nums, pivot + 1, end)

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quickSort(nums, 0, len(nums) - 1)


sol = Solution()
nums = [0, 1]
sol.sortColors(nums)
print(nums)

nums = [2,0,2,1,1,0]
sol.sortColors(nums)
print(nums)

nums = [2,0,1]
sol.sortColors(nums)
print(nums)

nums = [0]
sol.sortColors(nums)
print(nums)

nums = [1]
sol.sortColors(nums)
print(nums)