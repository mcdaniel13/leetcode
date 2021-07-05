from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            # print("l =", l, "r =", r, "num[l] =", nums[l], "num[r] =", nums[r])
            if nums[l] == target:
                # print("nums[l] == target")
                return l
            elif nums[r] == target:
                # print("nums[r] == target")
                return r
            else:
                m = int((l + r) / 2)
                # print("m = ", m, "nums[m] =", nums[m])
                if nums[m] == target:
                    return m
                if nums[l] > nums[r]:
                    l += 1
                    r -= 1
                else:
                    if nums[m] > target:
                        l += 1
                        r = m - 1
                    else:
                        l = m + 1
                        r -= 1

        return -1

sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))
print(sol.search([4,5,6,7,0,1,2], 3))
print(sol.search([1], 0))