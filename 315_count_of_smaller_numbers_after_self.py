from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = [(nums[i], i) for i in range(len(nums))]
        res = [0] * len(nums)
        self.merge_sort(nums, res, 0, len(nums) - 1)

        return res

    def merge_sort(self, nums: List[tuple], res: List[int], l: int, r: int) -> None:
        if l >= r:
            return

        mid = int((l + r) / 2)
        self.merge_sort(nums, res, l, mid)
        self.merge_sort(nums, res, mid + 1, r)
        self.merge(nums, res, l, mid, r)

    def merge(self, nums: List[tuple], res: List[int], l: int, mid: int, r: int) -> None:
        nums_l = [nums[i] for i in range(l, mid + 1)]
        nums_r = [nums[i] for i in range(mid + 1, r + 1)]
        idx_l = idx_r = idx = 0
        while idx_l < len(nums_l) and idx_r < len(nums_r):
            if nums_l[idx_l][0] <= nums_r[idx_r][0]:
                nums[idx + l] = nums_l[idx_l]
                res[nums[idx + l][1]] += idx - idx_l
                idx_l += 1
            else:
                nums[idx + l] = nums_r[idx_r]
                idx_r += 1
            idx += 1

        while idx_l < len(nums_l):
            nums[idx + l] = nums_l[idx_l]
            res[nums[idx + l][1]] += idx - idx_l
            idx_l += 1
            idx += 1

        while idx_r < len(nums_r):
            nums[idx + l] = nums_r[idx_r]
            idx_r += 1
            idx += 1


sol = Solution()
print(sol.countSmaller([5, 3, 2, 6, 1]))
print(sol.countSmaller([5, 2, 6, 1]))
print(sol.countSmaller([-1]))
print(sol.countSmaller([-1, -1]))
