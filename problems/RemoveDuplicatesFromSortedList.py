from entities import ListNode


class Solution:
    """
        as is:
        1 -> 1-> 1-> 2

        after:
        1  1 -> 1 -> 2
        |____________^
    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head

        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next

        return head

    """
        as is:
        1 -> 1-> 1-> 2
        
        after:
        1    1   1   2
        |____________^            
    """
    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        cur = head

        while cur:
            while cur.next and cur.next.val == cur.val:
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = None
            cur = cur.next

        return head
