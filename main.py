from trees.search_bst import Solution, TreeNode

if __name__ == '__main__':
    s = Solution()

    root = TreeNode(4)

    root.left = TreeNode(2)
    root.right = TreeNode(7)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    print(s.searchBST(root, 2))