from linked_list.remove_elements import Solution, ListNode

if __name__ == '__main__':
    s = Solution()

    # head = ListNode(7)
    # node1 = ListNode(7)
    # node2 = ListNode(7)
    # node3 = ListNode(7)
    #
    # head.next = node1
    # node1.next = node2
    # node2.next = node3

    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(6)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    curr = s.removeElements(head, 6)
    # curr = s.removeElements(head, 7)

    while curr:
        print(curr.val)
        curr = curr.next
