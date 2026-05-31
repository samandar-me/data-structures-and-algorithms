from collections import deque

class TreeNode:
    def __init__(self, val:int=0, left=None, right=None):
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