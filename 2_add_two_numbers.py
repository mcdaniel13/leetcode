class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        cur = res
        added = False
        while l1:
            sum = l1.val + l2.val
            if added:
                sum += 1
                added = False

            if sum >= 10:
                added = True
                cur.val = sum - 10
            else:
                cur.val = sum

            l1 = l1.next
            l2 = l2.next

            if l2 is None:
                while l1:
                    cur.next = ListNode()
                    cur = cur.next
                    if added:
                        sum = l1.val + 1
                        added = False
                        if sum >= 10:
                            added = True
                            cur.val = sum - 10
                        else:
                            cur.val = sum

                        l1 = l1.next
                    else:
                        cur.val = l1.val
                        cur.next = l1.next
                        break
                if added:
                    cur.next = ListNode(1)
                    added = False
                break

            if l1:
                cur.next = ListNode()
                cur = cur.next

        while l2:
            cur.next = ListNode()
            cur = cur.next
            if added:
                sum = l2.val + 1
                added = False
                if sum >= 10:
                    added = True
                    cur.val = sum - 10
                else:
                    cur.val = sum

                l2 = l2.next
            else:
                cur.val = l2.val
                cur.next = l2.next
                break

        if added:
            cur.next = ListNode(1)

        return res


sol = Solution()

print(sol.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))),
                        ListNode(5, ListNode(6, ListNode(4)))))
print(sol.addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
                        ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
