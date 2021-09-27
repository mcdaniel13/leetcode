from typing import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def create(self, nums: List[int]) -> ListNode:
        head = ListNode()
        cur = head
        for i in range(len(nums)):
            cur.val = nums[i]
            if i != len(nums) - 1:
                cur.next = ListNode()
                cur = cur.next

        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1

        plus = 0
        while l1 and l2:
            val = l1.val + l2.val + plus
            plus = 0
            if val >= 10:
                plus = 1

            l1.val = val % 10
            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
            else:
                break
        if l1.next:
            l1 = l1.next
            while l1:
                val = l1.val + plus
                plus = 0
                if val >= 10:
                    plus = 1
                l1.val = val % 10
                if l1.next:
                    l1 = l1.next
                else:
                    break

        if l2.next:
            l2 = l2.next
            l1.next = l2
            while l2:
                val = l2.val + plus
                plus = 0
                if val >= 10:
                    plus = 1
                l2.val = val % 10
                if l2.next:
                    l2 = l2.next
                else:
                    break

            l1 = l2

        if plus:
            l1.next = ListNode(1)


        return head


sol = Solution()
l1 = sol.create([9, 9, 9, 9, 9, 9, 9])
l2 = sol.create([9, 9, 9, 9])
print(sol.addTwoNumbers(l2, l1))
