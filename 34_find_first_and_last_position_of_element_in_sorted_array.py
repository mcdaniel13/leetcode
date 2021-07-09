from typing import List


class Solution:
    def binarySearch(self, nums: List[int], target: int, ran: List[int], l: int, r: int) -> None:
        if l > r:
            # print("l >= r")
            return

        if nums[l] == target:
            ran[0] = min(ran[0], l)
            ran[1] = max(ran[1], l)
            # print(ran)
        if nums[r] == target:
            ran[0] = min(ran[0], r)
            ran[1] = max(ran[1], r)
            # print(ran)

        m = int((l + r) / 2)
        # print(" l =", l," r =", r," m =", m, " target =", target, " nums[m] =", nums[m])
        if nums[m] < target:
            l = m + 1
            # print("nums[m] < target l =", l, "r =", r)
            self.binarySearch(nums, target, ran, l, r)
        elif nums[m] > target:
            r = m - 1
            # print("nums[m] > target l =", l, "r =", r)
            self.binarySearch(nums, target, ran, l, r)
        else:
            # print("match at m =", m)
            ran[0] = min(ran[0], m)
            ran[1] = max(ran[1], m)
            # print(ran)
            self.binarySearch(nums, target, ran, m + 1, r)
            self.binarySearch(nums, target, ran, l, m - 1)


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        ran = [10e9 + 1, -(10e9 + 1)]
        # print(ran)
        self.binarySearch(nums, target, ran, l, r)
        # print("result =", ran)
        if ran[1] == -(10e9 + 1):
            return [-1, -1]

        return ran


sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))
print(sol.searchRange([5,7,7,8,8,10], 6))
print(sol.searchRange([], 0))