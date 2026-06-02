from collections import deque

class TreeNode:
    def __init__(self, val: int=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return TreeNode()

    new_node = root

    queue = deque([root])

    while queue:
        node = queue.popleft()

        print(node.val)

        if node.left:
            # new_node.right = node.left
            queue.append(node.left)
        if node.right:
            # new_node.left = node.right
            queue.append(node.right)

    return TreeNode()


def dfs(root: TreeNode) -> None:
    if not root:
        return

    print(root.val)

    dfs(root.left)
    dfs(root.right)

def bfs(root: TreeNode):
    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
     #   print(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

if __name__ == '__main__':
    t4 = TreeNode(4)
    t2 = TreeNode(2)
    t1 = TreeNode(1)
    t3 = TreeNode(3)
    t7 = TreeNode(7)
    t6 = TreeNode(6)
    t9 = TreeNode(9)

    t4.left = t2
    t4.right = t7

    t2.left = t1
    t2.right = t3

    t7.left = t6
    t7.right = t9

    print(invertTree(t4).val)
