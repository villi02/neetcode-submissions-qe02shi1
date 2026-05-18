# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkAndIterate(leftNode, rightNode):
            if (not leftNode) and rightNode:
                return False
            if (not rightNode) and leftNode:
                return False
            
            if (not rightNode) and (not leftNode):
                return True
            
            if leftNode.val != rightNode.val:
                return False
            
            return checkAndIterate(leftNode.left, rightNode.left) and checkAndIterate(leftNode.right, rightNode.right)
             
        return checkAndIterate(q, p)
            
            