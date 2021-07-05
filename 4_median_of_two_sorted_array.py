from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            return (nums[int(len(nums) / 2)] + nums[int(len(nums) / 2) - 1]) / 2
        else:
            return nums[int(len(nums) / 2)]


sol = Solution()

print(sol.findMedianSortedArrays([1, 3], [2]))
print(sol.findMedianSortedArrays([1, 2], [3, 4]))
print(sol.findMedianSortedArrays([0, 0], [0]))
print(sol.findMedianSortedArrays([], [1]))
print(sol.findMedianSortedArrays([2], []))
