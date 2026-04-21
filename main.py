class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def mergeTwoLists(head1: Node, head2: Node) -> Node:
    merged_head = None

    while head1.next is not None and head2.next is not None:
        n_min = min(head1.val, head2.next.val)
        n_max = max(head1.val, head2.next.val)

        merged_head.next = Node(n_min)
        merged_head.next.next = Node(n_max)

        head1 = head1.next
        head2 = head2.next

    return merged_head

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(4)
    n1.next = n2
    n2.next = n3

    n4 = Node(1)
    n5 = Node(3)
    n6 = Node(4)
    n4.next = n5
    n5.next = n6

    print(mergeTwoLists(n1, n4).val)