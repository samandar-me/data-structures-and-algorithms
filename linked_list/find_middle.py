# Finding the middle of a Linked List
#
# Given the head, find and return the middle node of the Linked List.
#
# If the Linked List is of even length, return the middle node on the right.

# Input: head = [1,2,3,4,5]
# Result: [3,4,5]
# Explanation: Since the node is returned, not the value in the middle, the answer 3 -> 4 -> 5 is correct.

# Input: head = [1,2,3,4,5,6]
# Result: [4,5,6]
# Explanation: Node(4) was returned instead of Node(3) because the length is even.

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