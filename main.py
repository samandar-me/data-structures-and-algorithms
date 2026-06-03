from collections import deque

from trees.same_tree import Solution

class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    sol = Solution()

    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)

    t2 = TreeNode(1)
    t2.left = TreeNode(2)
    t2.right = TreeNode(4)


    print(sol.isSameTree(t1, t2))
