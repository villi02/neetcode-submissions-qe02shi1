# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS

        def dfs(node, depth):
            if not node:
                return depth
            

            return max(dfs(node.left, depth+1), dfs(node.right, depth+1))
            """
            if not node.left and node.right:
                return dfs(node.right, depth+1)
            if not node.right and node.left:
                return dfs(node.left, depth+1)
            else:
                return depth
            """
        if not root:
            return 0
        return max(dfs(root.left, 1), dfs(root.right, 1))