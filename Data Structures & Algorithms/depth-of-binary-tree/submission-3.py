# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def DFS(i, node):
            if not node:
                return i
            

            return max(DFS(i+1, node.left), DFS(i+1, node.right))
        
    
        return DFS(0, root)
            
            