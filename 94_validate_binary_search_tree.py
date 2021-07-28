class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def checkValidation(self, node: TreeNode, min_node: TreeNode, max_node: TreeNode) -> bool:
        if node is None:
            return True

        if max_node is not None and node.val >= max_node.val:
            return False
        if min_node is not None and node.val <= min_node.val:
            return False

        return self.checkValidation(node.left, min_node, node) and self.checkValidation(node.right, node, max_node)


    def isValidBST(self, root: TreeNode) -> bool:
        return self.checkValidation(root, None, None)
