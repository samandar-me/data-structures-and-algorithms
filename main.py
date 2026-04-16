class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def middleNode(head: Node) -> Node:
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.next = node2
    node2.next = node3

    print(middleNode(node1).val)