class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        res = 0

    def find(self, root: TreeNode) -> int:
        if not root:
            return 0

        leftSum = max(self.find(root.left), 0)
        rightSum = max(self.find(root.right), 0)
        self.res = max(self.res, root.val + leftSum + rightSum)

        return max(leftSum, rightSum) + root.val

    def maxPathSum(self, root: TreeNode) -> int:
        self.res = root.val
        self.find(root)
        return self.res