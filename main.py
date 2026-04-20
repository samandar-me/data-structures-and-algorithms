class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def isPalindrome(head: Node) -> bool:
    revered_linked_list = reverse(head)
    return head.val == revered_linked_list.val


def reverse(head: Node) -> Node:
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous

        previous = current
        current = next_node

    return previous

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(2)
    n4 = Node(1)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    print(isPalindrome(n1))