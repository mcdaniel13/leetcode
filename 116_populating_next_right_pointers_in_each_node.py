class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect_next(self, root: 'Node', next_node: 'Node') -> None:
        if not root:
            return

        root.next = next_node
        self.connect_next(root.left, root.right)
        if root.next:
            self.connect_next(root.right, root.next.left)
        else:
            self.connect_next(root.right, None)

    def connect(self, root: 'Node') -> 'Node':
        self.connect_next(root, None)
        return root
