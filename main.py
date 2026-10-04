from linked_list.remove_nth_from_end import Solution, ListNode

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)

    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)

    head.next = two
    two.next = three
    three.next = four
    four.next = five

    curr = s.removeNthFromEnd(head, 2)

    print()
    print("main")
    while curr:
        print(curr.val)
        curr = curr.next