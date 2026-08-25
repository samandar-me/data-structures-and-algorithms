from arrays.missing_multiple import Solution

if __name__ == '__main__':
    s = Solution()
    print(s.missingMultiple(nums = [8,2,3,4,6], k = 2))

    # root = TreeNode(10)
    #
    # root.left = TreeNode(5)
    # root.right = TreeNode(-3)
    #
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(2)
    #
    # root.right.right = TreeNode(11)
    #
    # root.left.left.left = TreeNode(3)
    # root.left.left.right = TreeNode(-2)
    #
    # root.left.right.right = TreeNode(1)
    #
    # print(s.pathSum(root, 8))