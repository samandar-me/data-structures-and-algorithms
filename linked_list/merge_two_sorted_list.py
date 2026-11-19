class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        merged = dummy
        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                merged.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                merged.next = ListNode(curr2.val)
                curr2 = curr2.next

        print(dummy.next.val)

        while curr1:
            merged.next = ListNode(curr1.val)
            curr1 = curr1.next

        while curr2:
            merged.next = ListNode(curr2.val)
            curr2 = curr2.next

        return dummy.next