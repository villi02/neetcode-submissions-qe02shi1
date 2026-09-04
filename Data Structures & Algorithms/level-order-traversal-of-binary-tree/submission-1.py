# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Basically doing BFS and adding at each level

        res = []

        def BFS(node, i):
            if not node:
                return
            if len(res) < i+1:
                res.append([])
            
            res[i].append(node.val)

            BFS(node.left, i+1)
            BFS(node.right, i+1)
            return
        
        BFS(root, 0)
        return res