from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            cur_max = max_product * nums[i]
            cur_min = min_product * nums[i]
            max_product = max(nums[i], max(cur_min, cur_max))
            min_product = min(nums[i], min(cur_min, cur_max))
            res = max(res, max_product)

        return res


sol = Solution()
print(sol.maxProduct([-4, -3, -2]))
print(sol.maxProduct([2, 3, -2, 4]))
print(sol.maxProduct([-2, 0, 1]))
