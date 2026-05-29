from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        tail.next = list1 or list2


if __name__ == '__main__':
    l2 = ListNode(0)
    l3 = ListNode(3)
    l2.next = l3

    l1 = None

    solution = Solution()
    result = solution.mergeTwoLists(l1, l2)

    node = result
    while node:
        print(node.val)
        node = node.next
