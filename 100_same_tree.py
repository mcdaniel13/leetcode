class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and q:
            q = [[p, q]]
            while q:
                nodes = q.pop(0)
                if nodes[0].val != nodes[1].val:
                    return False

                if nodes[0].left and nodes[1].left:
                    q.append([nodes[0].left, nodes[1].left])
                elif (nodes[0].left and not nodes[1].left) or \
                        (not nodes[0].left and nodes[1].left):
                    return False

                if nodes[0].right and nodes[1].right:
                    q.append([nodes[0].right, nodes[1].right])
                elif (nodes[0].right and not nodes[1].right) or \
                        (not nodes[0].right and nodes[1].right):
                    return False
            return True
        else:
            return False
