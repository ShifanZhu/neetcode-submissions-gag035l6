# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0 # return val

        # depth first search
        def dfs(node):
            if not node:
                return 0

            left_dim = dfs(node.left)
            right_dim = dfs(node.right)

            self.ans = max(self.ans, left_dim + right_dim)

            return max(left_dim, right_dim) + 1

        # apply on root
        dfs(root)
        return self.ans
            