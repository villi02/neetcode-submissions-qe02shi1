# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head.next:
            return 

        count = head
        m = 0
        # Find the length
        while count:
            m += 1
            count = count.next
        
        second_head = head
        middle = None

        for _ in range((m+1)//2):
            middle = second_head
            second_head = second_head.next
        
        middle.next = None # seperate the halfs

        # second head is now in the middle
        # Now we simply reverse the second_head and then iterate

        curr = second_head
        prev = None
        nextt = second_head.next

        while nextt: # Reversing the second half
            curr.next = prev
            prev = curr
            curr = nextt
            nextt = nextt.next
        
        curr.next = prev

        head2 = curr
        nextt2 = head2.next
        
        nextt = head.next

        # Not we have two heads
        while nextt2 or nextt:
            head.next = head2
            head = nextt
            if nextt:
                nextt = nextt.next
            else:
                nextt = None

            head2.next = head
            head2 = nextt2
            if nextt2:
                nextt2 = nextt2.next
            else:
                nextt2 = None

        if head2:
            head.next = head2
