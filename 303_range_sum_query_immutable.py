from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.arr = [0] * (len(nums) + 1)
        for i in range(1, len(self.arr)):
            self.arr[i] = self.arr[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right + 1] - self.arr[left]