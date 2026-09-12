# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # do DFS and append to a list in that order, then simply extract the K-th element??

        res = []

        def DFS(node):
            if not node:
                return None
            

            DFS(node.left)
            res.append(node.val)
            DFS(node.right)
        
        DFS(root)
        print(res)

        return res[k-1]
