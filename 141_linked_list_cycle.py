class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cur = head
        while cur:
            if cur.val == pow(10, 5) + 1:
                return True
            cur.val = pow(10, 5) + 1
            cur = head.next

        return False

    def hasCycle2(self, head: ListNode) -> bool:
        nodeSet = set()
        node = head
        while node:
            if node in nodeSet:
                return True
            else:
                nodeSet.add(node)
                node = node.next

        return False
