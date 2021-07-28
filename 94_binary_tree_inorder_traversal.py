# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getInorder(self, node: TreeNode, res: List[int]) -> None:
        if node is None:
            return

        self.getInorder(node.left, res)
        res.append(node.val)
        self.getInorder(node.right, res)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.getInorder(root, res)
        return res