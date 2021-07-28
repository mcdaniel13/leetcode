from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums = nums1[:]
        if n == 0:
            return

        j1 = 0
        j2 = 0
        for i in range(m + n):
            if j1 == m:
                if j2 < n:
                    nums1[i:] = nums2[j2:n]
                break

            if j2 == n:
                if j1 < m:
                    nums1[i:] = nums[j1:m]
                break

            if nums[j1] > nums2[j2]:
                nums1[i] = nums2[j2]
                j2 += 1
            else:
                nums1[i] = nums[j1]
                j1 += 1


sol = Solution()

nums = [4, 0, 0, 0, 0, 0]
sol.merge(nums, 1, [1, 2, 3, 5, 6], 5)
print(nums)

nums = [2, 0]
sol.merge(nums, 1, [1], 1)
print(nums)

nums = [1, 2, 3, 0, 0, 0]
sol.merge(nums, 3, [2, 5, 6], 3)
print(nums)

nums = [1]
sol.merge(nums, 1, [], 0)
print(nums)

nums = [0]
sol.merge(nums, 0, [1], 1)
print(nums)
