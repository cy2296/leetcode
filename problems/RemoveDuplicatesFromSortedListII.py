from entities.ListNode import *


class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head

        pre, cur = dummy, head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            if pre.next == cur:  # no duplicates happened, move pre forward
                pre = cur
            else:
                pre.next = cur.next  # skip cur which is the last duplicate item
            cur = cur.next

        return dummy.next

    def deleteDuplicates2(self, head):
        dummy = ListNode(0)
        dummy.next = head

        pre, cur = dummy, head
        while cur:
            if cur.next and cur.next.val == cur.val:
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next

        return dummy.next


