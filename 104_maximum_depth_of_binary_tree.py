class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMaxDepth(self, node: TreeNode, depth: int) -> int:
        if node is None:
            return depth - 1

        return max(self.findMaxDepth(node.left, depth + 1), self.findMaxDepth(node.right, depth + 1))

    def maxDepth(self, root: TreeNode) -> int:
        return self.findMaxDepth(root, 1)