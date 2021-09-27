# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next

        n = len(arr)
        head = ListNode(0)
        cur = head
        for i in range(n // 2):
            cur.next = arr[i]
            cur = cur.next
            cur.next = arr[n - 1 - i]
            cur = cur.next

        if len(arr) % 2 == 0:
            cur.next = None
        else:
            cur.next = arr[n // 2]
            cur.next.next = None

        return



