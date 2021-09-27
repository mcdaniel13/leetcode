# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        for i in range(n):
            if cur.next:
                cur = cur.next
            else:
                return head.next

        nth = head
        while cur.next:
            nth = nth.next
            cur = cur.next

        nth.next = nth.next.next

        return head

    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next

        if len(arr) <= 1:
            return None

        if arr[-n] == arr[-1]:
            arr[-n - 1].next = None
        elif arr[-n] == arr[0]:
            head = arr[1]
        else:
            arr[-n - 1].next = arr[-n - 1].next.next
        return head

def createListNode(vals: List[int]) -> ListNode:
    head = ListNode()
    cur = head
    for i in range(len(vals)):
        cur.val = vals[i]
        if i < len(vals) - 1:
            cur.next = ListNode()
            cur = cur.next

    return head

sol = Solution()
print(sol.removeNthFromEnd(createListNode([1,2,3,4,5]), 2))
print(sol.removeNthFromEnd(createListNode([1]), 1))
print(sol.removeNthFromEnd(createListNode([1,2]), 1))
