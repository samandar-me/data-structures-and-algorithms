from typing import Optional

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = []

        current = head
        while current:
            result.append(str(current.val))
            current = current.next

        return int("".join(result), 2)

    # def getDecimalValue(self, head: Optional[ListNode]) -> int:
    #     binary = ""
    #
    #     current = head
    #     while current:
    #         binary += str(current.val)
    #         current = current.next
    #
    #     return int(binary, 2)

    # def getDecimalValue(self, head: Optional[ListNode]) -> int:
    #     l_sum = 0
    #
    #     curr = head
    #     while curr:
    #         l_sum = l_sum * 2 + curr.val
    #         curr = curr.next
    #
    #     return l_sum