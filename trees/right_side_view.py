from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])
        stack = []

        while queue:
            q_len = len(queue)

            if stack:
                result.append(stack.pop())

            for _ in range(q_len):
                node = queue.popleft()

                if node:
                    stack.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

        return result