from typing import Optional

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = even_head

        return head