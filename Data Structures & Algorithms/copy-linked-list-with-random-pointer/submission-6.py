"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def newNode(self, node):
        new = Node(node.val)
        return new

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        
        explored = {}
        explored[head] = self.newNode(head)

        newHead = explored[head]
        iter_head = newHead

        while head:
            rand_node = None
            next_node = None

            if head.next:
                if head.next not in explored:
                    next_node = self.newNode(head.next)
                    explored[head.next] = next_node
                else:
                    next_node = explored[head.next]
            

            if head.random:
                if head.random not in explored:
                    rand_node = self.newNode(head.random)
                    explored[head.random] = rand_node
                else:
                    rand_node = explored[head.random]
            
            iter_head.next = next_node
            iter_head.random = rand_node

            iter_head = iter_head.next
            head = head.next

        return newHead