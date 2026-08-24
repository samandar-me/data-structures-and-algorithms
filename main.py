from trees.has_path_sum import Solution, TreeNode

if __name__ == '__main__':
    s = Solution()

    root = TreeNode(5)

    root.left = TreeNode(4)
    root.right = TreeNode(8)

    root.left.left = TreeNode(11)

    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)

    root.right.right.right = TreeNode(1)

    print(s.hasPathSum(root, 22))