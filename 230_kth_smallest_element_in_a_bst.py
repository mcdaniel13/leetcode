from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def search(self, nums: List[int], cur: TreeNode) -> None:
        if cur.left:
            self.search(nums, cur.left)

        nums.append(cur.val)

        if cur.right:
            self.search(nums, cur.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        nums = []
        self.search(nums, root)

        return nums[k - 1]
