from typing import Optional

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        curr = head

        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head