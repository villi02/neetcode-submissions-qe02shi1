# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heads = []
        res = []
        head = ListNode()
        curr = head

        for i in range(len(lists)):
            node = lists[i]
            j = 0
            while node:
                heapq.heappush(heads, [node.val, i, j, node])
                node = node.next
                j += 1
        
        while heads:
            _,_,_, nxt = heapq.heappop(heads)
            curr.next = nxt
            curr = nxt
        
        return head.next
