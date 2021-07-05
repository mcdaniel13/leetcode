# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        vals = []
        for li in lists:
            while li:
                vals.append(li.val)
                li = li.next

        if len(vals) == 0:
            return None

        vals.sort()

        res = ListNode()
        cur = res
        for i in range(len(vals)):
            cur.val = vals[i]
            if i != len(vals) - 1:
                cur.next = ListNode()
                cur = cur.next

        return res

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
print(sol.mergeKLists([createListNode([1,4,5]), createListNode([1,3,4]), createListNode([2,6])]))
print(sol.mergeKLists([createListNode([])]))
print(sol.mergeKLists([]))
