import math
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        mid = math.ceil(len(nums) / 2)
        first_half = nums[:mid]
        second_half = nums[mid:]

        fi = len(first_half) - 1
        si = len(second_half) - 1
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = first_half[fi]
                fi -= 1
            else:
                nums[i] = second_half[si]
                si -= 1

        print(nums)


sol = Solution()
sol.wiggleSort([4, 5, 5, 6])
sol.wiggleSort([1, 2, 1, 2, 1, 1, 2, 2, 1])
sol.wiggleSort([1])
sol.wiggleSort([1, 5, 1, 1, 6, 4])
sol.wiggleSort([1, 3, 2, 2, 3, 1])
sol.wiggleSort([5, 5, 5, 4, 4, 4, 4])
