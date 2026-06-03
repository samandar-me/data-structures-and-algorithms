from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def symmetric(root1, root2) -> bool:
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    if root1.val != root2.val:
        return False

    return (symmetric(root1.left, root2.right) and
            symmetric(root1.right, root2.left))

def isSymmetric(root: TreeNode) -> bool:
    return symmetric(root, root)

# def isSymmetric(root: TreeNode) -> bool:
#     print(bfs(root))
#     print(bfs(invert(root)))
#
#     return bfs(root) == bfs(invert(root))
#
#
# def bfs(root: TreeNode) -> list:
#     if not root:
#         return []
#
#     result = []
#
#     queue = deque([root])
#
#     while queue:
#         node = queue.popleft()
#
#         if node:
#             result.append(node.val)
#             queue.append(node.left)
#             queue.append(node.right)
#         else:
#             result.append(None)
#
#     return result
#
#
# def invert(root: TreeNode) -> TreeNode:
#     dfs(root)
#
#     return root
#
#
# def dfs(root: TreeNode):
#     if not root:
#         return
#
#     root.left, root.right = root.right, root.left
#
#     dfs(root.left)
#     dfs(root.right)