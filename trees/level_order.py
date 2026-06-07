from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode) -> list:
    if not root:
        return []

    result = []

    queue = deque([root])

    while queue:
        q_len = len(queue)

        level = []

        for i in range(q_len):
            node = queue.popleft()

            print(f"i {i} ")

            if node:
                print(f"node {node.val} ")
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        if level:
            result.append(level)
        print()

    return result