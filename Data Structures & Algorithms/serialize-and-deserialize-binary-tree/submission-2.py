# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def DFS(curr, res):
            if not curr:
                return res + "N,"
            if curr:
                # val if val, N else
                # e.g. 2, 3, 4, N

                val = curr.val
                res += f"{val}," + DFS(curr.left, res) + DFS(curr.right, res)
                
                
            return res

        return DFS(root, "")
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        Root = TreeNode()
        curr = Root
        nodes = data.split(",")

        dfs = deque(nodes)

        def DFS(queue):
            if not queue:
                return None

            new = queue.popleft()
            if new == "N":
                return None
            
            newNode = TreeNode(new)

            newNode.left = DFS(queue)
            newNode.right = DFS(queue)
            return newNode

        return DFS(dfs)