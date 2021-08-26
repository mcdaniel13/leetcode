from typing import List


class Solution:
    # Time Complexity: O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        return not len(numSet) == len(nums)

    # Time Complexity: O(n)
    def containDuplicate2(self, nums: List[int]) -> bool:
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            else:
                numSet.add(num)

        return False


sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 1]))
print(sol.containsDuplicate([1, 2, 3, 4]))
print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
