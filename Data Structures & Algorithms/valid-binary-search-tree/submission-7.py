# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_iter(node, minVal, maxVal):
            if not minVal < node.val < maxVal:
                return False
            if not node.left and not node.right:
                return True
            if not node.left:
                if node.val < node.right.val:
                    return check_iter(node.right, node.val, maxVal)
                else:
                    return False
            if not node.right:
                if node.val > node.left.val:
                    return check_iter(node.left, minVal, node.val)
                else:
                    return False

            

            if minVal < node.left.val < node.val and node.val < node.right.val < maxVal:
                return check_iter(node.left, minVal, node.val) and check_iter(node.right, node.val, maxVal)
            
            return False

        return check_iter(root, -float("infinity"), float("infinity"))