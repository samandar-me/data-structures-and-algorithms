class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        stack = [(root, float("-inf"))]

        while stack:
            node, largest = stack.pop()

            if largest <= node.val:
                counter += 1

            largest = max(node.val, largest)

            if node.right:
                stack.append((node.right, largest))
            if node.left:
                stack.append((node.left, largest))

        return counter