from typing import List


class comp(str):
    def __lt__(a, b):
        return a + b > b + a


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_to_str = [str(num) for num in nums]
        res = sorted(nums_to_str, key=comp)

        if list(set(res)) == ['0']:
            return '0'

        return "".join(res)


sol = Solution()
print(sol.largestNumber([10, 2]))
print(sol.largestNumber([3, 30, 34, 5, 9]))
print(sol.largestNumber([1]))
print(sol.largestNumber([10]))
