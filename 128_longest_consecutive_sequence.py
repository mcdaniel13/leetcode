from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        prev = nums[0]
        cnt = 1
        res = 0
        for num in nums:
            if prev + 1 == num:
                cnt += 1
                prev = num
            elif prev == num:
                continue
            else:
                res = max(res, cnt)
                prev = num
                cnt = 1

        return max(res, cnt)


sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
