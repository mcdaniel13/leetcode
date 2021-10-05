class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next

        temp = None
        for i in range(0, len(arr), 2):
            if i + 1 >= len(arr):
                temp.next = arr[i]
                temp = arr[i]
                break

            if temp:
                temp.next = arr[i + 1]
            arr[i + 1].next = arr[i]
            temp = arr[i]

        if temp:
            temp.next = None

        return arr[1]
