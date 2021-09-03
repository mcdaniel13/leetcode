class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        mini, maxi = min(p.val, q.val), max(p.val, q.val)
        while root:
            if root.val < mini:
                root = root.right
            elif root.val > maxi:
                root = root.left
            else:
                break

        return root
