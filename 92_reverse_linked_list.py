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

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next and left == right:
            return head

        arr = [None]
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        arr.append(None)

        for i in range(right, left - , -1):
            arr[i].next = arr[i - 1]

        if arr[left - 1]:
            arr[left - 1].next = arr[right]

        if arr[right + 1]:
            arr[left].next = arr[right + 1]
        else:
            arr[left].next = None

        return arr[1]

sol = Solution()
l = sol.create([3, 5])
sol.reverseBetween(l, 1, 2)
