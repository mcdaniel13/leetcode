class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = [[root, 1]]
        res = sys.maxsize
        while q:
            cur = q.pop(0)
            node = cur[0]
            level = cur[1]
            if not node.left and not node.right:
                res = min(res, level)

            if level < res:
                if node.left:
                    q.append([node.left, level + 1])
                if node.right:
                    q.append([node.right, level + 1])

        return res
