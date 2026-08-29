# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_iter(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return (check_iter(left.left, right.left)) and (check_iter(left.right, right.right))


        # Think we can just go through the root and find any nodes that have the root of the subtree and iteratively check them

        if not subRoot:
            return False
        if not root:
            return False

        matching_roots = []

        iter_root = root

        nodes = deque()

        nodes.append(root)
        current = None
        while nodes:
            current = nodes.popleft()

            if current.left:
                nodes.append(current.left)
            if current.right:
                nodes.append(current.right)

            if current.val == subRoot.val:
                #matching_roots.append(current)
                if check_iter(current, subRoot):
                    return True
        
        return False

            
        # Now we have a full potential matching_roots

        #for rt in matching_roots: # Iterate through all the nodes to see if they match
            #subrt = subRoot

            #if 
        
            