from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def build(self, nums: List[int]) -> ListNode:
        if len(nums) == 0:
            return None

        head = ListNode(nums[0])
        cur = head
        for i in range(1, len(nums)):
            cur.next = ListNode(nums[i])
            cur = cur.next
        return head

    def print(self, head: ListNode) -> List[int]:
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next

        return res


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        li = []
        cur = head
        while cur:
            li.append(cur)
            cur = cur.next

        new_head = li[-1]
        cur = new_head
        for i in range(len(li) - 2, -1, -1):
            cur.next = li[i]
            cur = cur.next
        cur.next = None
        return new_head


sol = Solution()
head = LinkedList().build([1, 2, 3, 4, 5])
head = sol.reverseList(head)
print(LinkedList().print(head))

head = LinkedList().build([1, 2])
head = sol.reverseList(head)
print(LinkedList().print(head))
