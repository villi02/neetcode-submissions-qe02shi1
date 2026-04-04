# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # We probably want to just have two pointers, one fast and one slow, if they are ever on the same node, then it is a cycle
        slow, fast = head, head.next

        i = 0
        while slow and fast:
            fast = fast.next

            if i % 2 == 0:
                slow = slow.next

            i += 1

            if (fast == slow) and (fast.next == slow.next):
                return True

        return False