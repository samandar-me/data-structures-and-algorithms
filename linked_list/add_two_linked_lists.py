from typing import Optional

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        total_sum = self.extract_num(l1) + self.extract_num(l2)

        if total_sum == 0:
            return l1

        head = None
        tail = None

        while total_sum > 0:
            node = ListNode(total_sum % 10)

            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node

            total_sum //= 10

        return head


    def extract_num(self, head: Optional[ListNode]) -> int:
        curr = head
        num = 0
        while curr:
            num = num * 10 + curr.val
            curr = curr.next

        return num

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous