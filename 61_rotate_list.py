class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        k %= len(arr)
        head = arr[-k]
        arr[-1].next = arr[0]
        arr[-(k + 1)].next = None
        return head
