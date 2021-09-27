class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s = set()
        cur = head
        while cur:
            if cur in s:
                return cur
            s.add(cur)
            cur = cur.next

        return None
