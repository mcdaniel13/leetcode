class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        cnt = []
        q = [[root, 0]]
        while q:
            cur = q.pop(0)
            node = cur[0]
            level = cur[1]
            if len(res) - 1 >= level:
                res[level] = (res[level] * cnt[level] + node.val) / (cnt[level] + 1)
                cnt[level] += 1
            else:
                res.append(node.val)
                cnt.append(1)

            if node.left:
                q.append([node.left, level + 1])
            if node.right:
                q.append([node.right, level + 1])

        return res
