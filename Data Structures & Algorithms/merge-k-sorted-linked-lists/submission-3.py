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

        count = 0
        for lis in lists:
            if lis:
                heapq.heappush(heads, [lis.val,count, lis])
                count += 1
        
        while heads:
            _,_, nxt = heapq.heappop(heads)
            curr.next = nxt
            curr = nxt
            if nxt.next:
                heapq.heappush(heads, [nxt.next.val, count, nxt.next])
                count += 1
        
        return head.next