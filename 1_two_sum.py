from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, val1 in enumerate(nums):
            for idx2, val2 in enumerate(nums[idx1 + 1:], idx1 + 1):
                if val1 + val2 == target:
                    return [idx1, idx2]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        numDict = dict()
        for i in range(len(nums)):
            if nums[i] in numDict:
                return [numDict[nums[i]], i]
            numDict[target - nums[i]] = i
        return [-1, -1]

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        arr = [(nums[i], i) for i in range(len(nums))]
        start = 0
        end = len(nums) - 1
        arr.sort()
        while start < end:
            sum = arr[start][0] + arr[end][0]
            if sum < target:
                start += 1
            elif sum > target:
                end -= 1
            else:
                break


        return [arr[start][1], arr[end][1]]


sol = Solution()

print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([3, 2, 4], 6))
print(sol.twoSum([3, 3], 6))


