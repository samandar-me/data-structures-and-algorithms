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