# Time Complexity: O(nlog(n))
# Space Complexity: O(n)

from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)


sol = Solution()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(sol.lengthOfLIS([0,1,0,3,2,3]))
print(sol.lengthOfLIS([7,7,7,7,7,7,7]))