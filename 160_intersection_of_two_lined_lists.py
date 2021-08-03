class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_set = set()
        cur = headA
        while cur:
            node_set.add(cur)
            cur = cur.next

        cur = headB
        while cur:
            if cur in node_set:
                return cur
            cur = cur.next

        return None