class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        odd_head = head.next
        even = head.next

        node = head.next
        while node and node.next:
            node = node.next
            odd.next = node
            odd = odd.next
            even.next = node.next
            even = even.next
            node = node.next

        odd.next = odd_head

        return head
