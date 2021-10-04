class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        prev = None
        cnt = 1
        while cur:
            if cnt == left:
                start = cur
                break
            prev = cur
            cur = cur.next
            cnt += 1

        arr = []
        while cur:
            arr.append(cur)
            if cnt == right:
                end = cur
                break
            cur = cur.next
            cnt += 1

        next = cur.next
        for i in range(len(arr) - 1, 0, -1):
            arr[i].next = arr[i - 1]

        if prev:
            prev.next = arr[-1]
        else:
            head = arr[-1]

        if next:
            arr[0].next = next
        else:
            arr[0].next = None

        return head