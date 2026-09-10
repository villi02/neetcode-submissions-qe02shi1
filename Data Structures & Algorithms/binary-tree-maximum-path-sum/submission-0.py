# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Need to find the maximum path sum of each node recursively i think
        # Then keep track of the min
        # Map it onto the other path problem that we have solved
        if not root:
            return 0

        maxSum = [root.val]

        def DFS(node):
            if not node:
                return 0
            
            maxL = max(DFS(node.left),0)
            maxR = max(DFS(node.right), 0)

            maxSum[0] = max(maxSum[0], node.val + maxL + maxR)
            return node.val + max(maxL, maxR)


        DFS(root)

        return maxSum[0]