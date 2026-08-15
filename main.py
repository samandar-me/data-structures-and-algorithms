from linked_list.delete_middle import Solution, ListNode

if __name__ == '__main__':
    s = Solution()

    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(5)
    node3 = ListNode(9)
    node4 = ListNode(11)
    node5 = ListNode(25)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node4.next = node5

    curr = s.deleteMiddle(head)

    while curr:
        print(curr.val)
        curr = curr.next
