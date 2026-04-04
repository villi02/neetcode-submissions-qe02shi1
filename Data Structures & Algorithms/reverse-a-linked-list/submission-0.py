# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        if head:
            current = head
            i = 0
            while current:
                oldNext = current.next
                current.next = newHead
                newHead = current
                current = oldNext

        return newHead