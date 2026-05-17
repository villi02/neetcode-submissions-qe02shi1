# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dfs = deque()
        dfs.append(root)

        if not root:
            return root

        while dfs:
            node = dfs.pop()

            if not node.right or not node.left:
                left = node.left if node.left else None
                right = node.right if node.right else None
                node.left = right
                node.right = left
            else:
                node.left, node.right = node.right, node.left
            if node.left:
                dfs.append(node.left)
            if node.right:
                dfs.append(node.right)

        return root