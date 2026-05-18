# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkAndIterate(leftNode, rightNode):
            
            if (not rightNode) and (not leftNode):
                return True
            if rightNode and leftNode and leftNode.val == rightNode.val:
                return checkAndIterate(leftNode.left, rightNode.left) and checkAndIterate(leftNode.right, rightNode.right)
            else:
                return False
             
        return checkAndIterate(q, p)
            
            