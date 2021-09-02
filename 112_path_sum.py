class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        self.dfs(root, 0, targetSum)
        return self.res

    def dfs(self, root: Optional[TreeNode], currentSum: int, targetSum: int) -> None:
        if self.res:
            return

        if not root.left and not root.right:
            self.res = currentSum + root.val == targetSum

        if root.left:
            self.dfs(root.left, currentSum + root.val, targetSum)

        if root.right:
            self.dfs(root.right, currentSum + root.val, targetSum)
