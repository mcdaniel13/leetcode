class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head

        odd_head = head
        even_head = head.next

        odd = head
        even = head.next
        cur = head.next.next
        while cur and cur.next:
            odd.next = cur
            even.next = cur.next
            cur = cur.next.next
            odd = odd.next
            even = even.next

        if cur:
            odd.next = cur
            odd = odd.next
            even.next = None
        odd.next = even_head

        return odd_head
