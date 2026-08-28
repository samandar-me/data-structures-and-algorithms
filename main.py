from trees.sum_numbers import Solution, TreeNode

if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)

    left = TreeNode(2)
    right = TreeNode(3)

    root.left = left
    root.right = right

    print(s.sumNumbers(root))