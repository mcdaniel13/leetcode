# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = res = nums[0]
        
        for i in range(1, len(nums)):
            cur = nums[i]
            tempMax = max(cur, max(curMax * cur, curMin * cur))
            curMin = min(cur, min(curMax * cur, curMin * cur))

            curMax = tempMax
            res = max(curMax, res)
            
        return res