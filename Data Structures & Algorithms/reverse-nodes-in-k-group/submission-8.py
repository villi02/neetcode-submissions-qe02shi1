# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        def reverseSSL(start, end, LeftSent, RightSent):
            tail = start
            head = end
            curr = start.next
            prev = start

            while curr != end and prev != end:
                nxt = curr.next
                curr.next = prev
            
                prev = curr
                curr = nxt
            
            LeftSent.next = end
            end.next = prev
            start.next = RightSent
            return

        node = head
        count = 0
        back = head
        backSent = head

        while node:
            count += 1
            if count == k:
                head = node
            if (count % k) == 0:
            
                nxt = node.next
                reverseSSL(back, node, backSent, nxt)
                backSent = back
                back = nxt
                node = nxt
            else:
                node = node.next
        return head