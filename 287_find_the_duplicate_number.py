from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_set = set()
        for i in range(len(nums)):
            if nums[i] in num_set:
                return nums[i]
            else:
                num_set.add(nums[i])

        return -1

    def findDuplicate2(self, nums: List[int]) -> int:
        flag = [False] * len(nums)

        i = 0
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return nums[i]


sol = Solution()
print(sol.findDuplicate2([1, 3, 4, 2, 2]))
print(sol.findDuplicate2([3, 1, 3, 4, 2]))
print(sol.findDuplicate2([1, 1]))
print(sol.findDuplicate2([1, 1, 2]))
