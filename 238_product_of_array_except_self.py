from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = nums[0]
        zero_cnt = 0
        if nums[0] == 0:
            zero_cnt = 1
        for i in range(1, len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zero_cnt += 1

        res = []
        for i in range(len(nums)):
            if zero_cnt > 0:
                if nums[i] == 0 and zero_cnt - 1 == 0:
                    res.append(product)
                else:
                    res.append(0)
            else:
                res.append(int(product/nums[i]))

        return res

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = r = 1
        res = [1] * n

        for i in range(n):
            res[i] *= l
            l *= nums[i]

            res[n - 1 - i] *= r
            r *= nums[n - 1 - i]

        return res

sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
print(sol.productExceptSelf([-1, 1, 0, -3, 3]))
