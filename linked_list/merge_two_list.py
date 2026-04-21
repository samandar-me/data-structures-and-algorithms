class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def mergeTwoLists(head1: Node, head2: Node) -> Node:
    n_max = max(head1.val, head2.val)
    return Node(n_max)