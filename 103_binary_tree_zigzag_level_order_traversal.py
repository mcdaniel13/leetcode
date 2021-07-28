from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        que = []
        res = []
        que.append([root, 0])
        lev = [0]
        while len(que) != 0:
            node = que.pop(0)
            if node[1] == lev[0]:
                lev.append(node[0].val)
            else:
                if lev[0] % 2 == 0:
                    res.append(lev[1:])
                else:
                    res.append(reversed(lev[1:]))
                lev = [node[1], node[0].val]
            if node[0].left is not None:
                que.append([node[0].left, node[1] + 1])
            if node[0].right is not None:
                que.append([node[0].right, node[1] + 1])

        if lev[0] % 2 == 0:
            res.append(lev[1:])
        else:
            res.append(reversed(lev[1:]))

        return res