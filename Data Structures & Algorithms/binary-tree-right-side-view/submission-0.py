# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # This is basically BFS, taking the rightmost node at each level
        # Can probably use DFS too

        res = []

        def BFS(node, level):
            if not node:
                return None
            if level == len(res):
                res.append(node.val)
            
            BFS(node.right, level+1)
            BFS(node.left, level+1)
        
        BFS(root, 0)

        return res