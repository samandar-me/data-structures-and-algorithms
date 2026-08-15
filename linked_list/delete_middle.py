from functools import cache
from typing import Optional

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return None

        slow = head
        fast = slow.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return head


    # def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     index_counter1 = 0
    #     index_counter2 = 0
    #
    #     curr = head
    #
    #     while curr:
    #         curr = curr.next
    #         index_counter1 += 1
    #
    #     if index_counter1 == 1:
    #         head = None
    #         return head
    #
    #     curr = head
    #
    #     dummy = ListNode()
    #     copy_tail = dummy
    #
    #     while curr:
    #         copy_tail.next = ListNode(curr.val)
    #         copy_tail = copy_tail.next
    #
    #         if index_counter2 == (index_counter1 // 2) - 1:
    #             curr = curr.next.next
    #         else:
    #             curr = curr.next
    #         index_counter2 += 1
    #
    #     return dummy.next