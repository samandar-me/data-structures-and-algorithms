class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


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
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    print(reverse(n1).val)