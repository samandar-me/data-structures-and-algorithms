from collections import deque

from trees.same_tree import Solution

class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root: TreeNode):
    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()

        print(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def dfs(root: TreeNode):
    if not root:
        return

    print(root.val)

    dfs(root.left)
    dfs(root.right)


if __name__ == '__main__':
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    dfs(root)

