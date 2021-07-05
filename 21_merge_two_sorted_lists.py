# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        cur = head
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next

        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2

        return head.next


def createListNode(vals: List[int]) -> ListNode:
    head = ListNode(-1)
    cur = head
    for i in range(len(vals)):
        cur.val = vals[i]
        if i < len(vals) - 1:
            cur.next = ListNode()
            cur = cur.next

    return head


sol = Solution()
print(sol.mergeTwoLists(createListNode([1, 2, 4]), createListNode([1, 3, 4])))
print(sol.mergeTwoLists(createListNode([]), createListNode([])))
print(sol.mergeTwoLists(createListNode([]), createListNode([0])))
