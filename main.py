from trees.path_sum_3 import Solution, TreeNode

if __name__ == '__main__':
    s = Solution()

    root = TreeNode(10)

    root.left = TreeNode(5)
    root.right = TreeNode(-3)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)

    root.right.right = TreeNode(11)

    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)

    root.left.right.right = TreeNode(1)

    print(s.pathSum(root, 8))