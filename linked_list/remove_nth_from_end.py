class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        if n == length:
            return head.next

        curr = head
        index = 0
        while curr:
            if index == length - n - 1:
                print(curr.val)
                curr.next = curr.next.next
                break
            curr = curr.next
            index += 1

        return head