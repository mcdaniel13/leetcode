# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getInorder(self, node: TreeNode, res: List[int], depth: int) -> None:
        if node is None:
            res.append(1000+depth)
            return

        self.getInorder(node.left, res, depth + 1)
        res.append(node.val)
        self.getInorder(node.right, res, depth + 1)

    def getReverseInOrder(self, node: TreeNode, res: List[int], depth: int) -> None:
        if node is None:
            res.append(1000+depth)
            return

        self.getReverseInOrder(node.right, res, depth + 1)
        res.append(node.val)
        self.getReverseInOrder(node.left, res, depth + 1)

    def isSymmetric(self, root: TreeNode) -> bool:
        res = []
        res1 = []
        self.getInorder(root.left, res, 0)
        self.getReverseInOrder(root.right, res1, 0)
        return res == res1