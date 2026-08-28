# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.balanced = True

        def dfs(node, height):
            if not node:
                return height
            
            height += 1
            left = dfs(node.left, height)
            right = dfs(node.right, height)

            if abs(left - right) > 1:
                self.balanced = False
            return max(left, right)
        
        startH = 0
        dfs(root, startH)
        return self.balanced
            