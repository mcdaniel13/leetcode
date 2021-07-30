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
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next

        arr = sorted(arr, key=lambda value: value.val)

        for i in range(len(arr) - 1):
            arr[i].next = arr[i + 1]

        arr[-1].next = None

        return arr[0]


sol = Solution()
head = LinkedList().build([4, 2, 1, 3])
head = sol.sortList(head)
print(LinkedList().print(head))
