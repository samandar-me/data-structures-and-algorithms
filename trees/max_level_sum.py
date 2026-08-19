from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        current_level = 0
        level_max = 1
        max_level_value = root.val
        queue = deque([root])

        while queue:
            current_level += 1
            q_len = len(queue)
            level_sum = 0

            for _ in range(q_len):
                node = queue.popleft()
                level_sum += node.val
                print(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if max_level_value < level_sum:
                max_level_value = level_sum
                level_max = current_level

        return level_max