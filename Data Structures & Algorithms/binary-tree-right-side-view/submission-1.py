# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Trying BFS solution

        res = []

        nodes = deque()
        nodes.append(root)

        while nodes:
            rightSide = None

            for i in range(len(nodes)):
                node = nodes.popleft()
                if node:
                    rightSide = node
                    nodes.append(node.left)
                    nodes.append(node.right)
            if rightSide:
                res.append(rightSide.val)


        return res


