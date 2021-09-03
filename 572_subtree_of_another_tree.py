class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.rootPreOrder = []
        self.subrootPreOrder = []

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.preOrder(root, self.rootPreOrder)
        self.preOrder(subRoot, self.subrootPreOrder)

        for i in range(len(self.rootPreOrder) - len(self.subrootPreOrder) + 1):
            if self.rootPreOrder[i:i + len(self.subrootPreOrder)] == self.subrootPreOrder:
                return True

        return False

    def preOrder(self, root: Optional[TreeNode], arr: List[int]):
        if not root:
            arr.append(None)
            return

        arr.append(root.val)
        self.preOrder(root.left, arr)
        self.preOrder(root.right, arr)
