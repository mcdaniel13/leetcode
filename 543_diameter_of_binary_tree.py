class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0

        leftVal = -1
        rightVal = -1
        if root.left:
            leftVal = self.dfs(root.left)
        if root.right:
            rightVal = self.dfs(root.right)

        self.res = max(leftVal + rightVal + 2, self.res)
        return max(leftVal + 1, rightVal + 1)
