# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # just pick the smallest of the available nodes and continue until None
        if not list1:
            return list2 if list2 else None
        if not list2:
            return list1 if list1 else None
        
        # Need to pick the head first
        # We know both list1 and list2 have a starting node here
        newHead = None

        if list1.val > list2.val:
            newHead = list2
            list2 = list2.next
        else:
            newHead = list1
            list1 = list1.next
        current = newHead

        # Double check that there was more than one element in the list
        if not list1:
            current.next = list2
            return newHead
        if not list2:
            current.next = list1
            return newHead

        while list1 and list2:
            # Simply pick the smallest node
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            
            current = current.next
            
            # Check if one of the pointers to the list nodes have become None
            if not list1:
                current.next = list2
                return newHead
            if not list2:
                current.next = list1
                return newHead
        return newHead
