# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_res = ListNode()
        carry = 0
        cur = l_res

        while l1 or l2:
            var1, var2 = 0, 0

            if l1:
                var1 = l1.val
                l1 = l1.next
            if l2:
                var2 = l2.val
                l2 = l2.next
            
            new = var1 + var2 + carry

            carry = new // 10
            new = new % 10
            
            cur.val = new
            if l1 or l2:
                cur.next = ListNode()
                cur = cur.next
        
        if carry > 0:
            cur.next = ListNode(val=carry)

        return l_res
            