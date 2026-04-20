class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def isPalindrome(head: Node) -> bool:
    revered_linked_list = reverse(head)
    return head == revered_linked_list


def reverse(head: Node) -> Node:
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous

        previous = current
        current = next_node

    return previous