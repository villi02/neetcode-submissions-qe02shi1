# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Just navigate down and keep track of the greatest node met until then?
        # Just use recursion

        self.res = 0

        def BFS(node, greatest):
            if not node:
                return None
            
            if node.val >= greatest:
                self.res += 1
            
            greatest = max(greatest, node.val)
            
            
            BFS(node.left, greatest)
            BFS(node.right, greatest)
        
        BFS(root, float("-infinity"))

        return self.res