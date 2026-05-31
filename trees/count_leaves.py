class TreeNode:
    def __init__(self, val: int=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_leaves(root: TreeNode) -> int:
    if not root:
        return 0

    counter = 0

    stack = [root]

    while stack:
        node = stack.pop()

        if is_leaf(node):
            counter += 1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return counter

# def count_leaves(root: TreeNode) -> int:
#     if not root:
#         return 0
#
#     if is_leaf(root):
#         return 1
#
#     return count_leaves(root.left) + count_leaves(root.right)

def is_leaf(node: TreeNode) -> bool:
    return node.left is None and node.right is None