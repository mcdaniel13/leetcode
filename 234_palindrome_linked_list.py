class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        return nums == nums[::-1]

    def isPalindrome2(self, head: ListNode) -> bool:
        s = ""
        fast = head
        slow = head
        while fast and fast.next:
            s += str(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast and not fast.next:  # odd
            slow = slow.next

        i = -1

        while slow:
            if int(s[i]) != slow.val:
                return False
            slow = slow.next
            i -= 1

        return True