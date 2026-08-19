from trees.right_side_view import Solution, TreeNode

if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)

    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    root.left = node2
    root.right = node3

    node2.left = node4

    node4.left = node5

    print(s.rightSideView(root))