from trees.max_level_sum import Solution, TreeNode

if __name__ == '__main__':
    s = Solution()

    root = TreeNode(989)

    node2 = TreeNode(10250)

    node3 = TreeNode(98693)
    node4 = TreeNode(-89388)
    node5 = TreeNode(-32127)

    root.right = node2

    node2.left = node3
    node2.right = node4

    node4.right = node5

    print(s.maxLevelSum(root))