# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None

        m = 0
        cnt = head

        while cnt:
            m += 1
            cnt = cnt.next
        
        index = m - n

        prev = None
        nextt = None
        curr = head

        for _ in range(index):
            prev = curr
            curr = curr.next
        
        nextt = curr.next

        # Now we need to disconnect current and let the others connect
        if prev:
            prev.next = nextt
        else:
            head = head.next
        curr.next = None
        return head