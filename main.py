from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    root = TreeNode(3)

    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(12)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)



