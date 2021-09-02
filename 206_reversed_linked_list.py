class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        li = []
        cur = head
        while cur:
            li.append(cur)
            cur = cur.next

        new_head = li[-1]
        cur = new_head
        for i in range(len(li) - 2, -1, -1):
            cur.next = li[i]
            cur = cur.next
        cur.next = None
        return new_head

    def reverseList2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        prev = head
        node = head.next
        next = head.next.next
        head.next = None

        while node:
            node.next = prev
            prev = node
            node = next
            if next:
                next = next.next

        return prev