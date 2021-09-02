# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        newHead = ListNode()
        newHead.next = head
        prev = newHead
        node = head
        while node:
            if node.val == val:  # remove node
                prev.next = node.next
            else:
                prev = node
            node = node.next

        return newHead.next
