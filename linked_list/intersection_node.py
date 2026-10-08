from typing import Optional

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA and not headB:
            return None

        intersection = None
        curr1, curr2 = self.reverse(headA), self.reverse(headB)

        while curr1 or curr2:
            if curr1 != curr2:
                break
            intersection = headA
            curr1 = curr1.next
            curr2 = curr2.next

        return intersection

    def reverse(self, head: ListNode) -> Optional[ListNode]:
        previous = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = previous
            previous = curr
            curr = next_node

        return previous