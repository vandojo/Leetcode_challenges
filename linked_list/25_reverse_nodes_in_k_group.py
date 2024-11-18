'''Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.'''


# SOLUTION

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reverse(self, head, k):
        prev = None
        curr = head
        
        for i in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev, curr
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy
        
        while ptr is not None:
            tracker = ptr
            
           
            for j in range(k):
                tracker = tracker.next
                if tracker is None:
                    return dummy.next 
            
            
            prev, curr = self.reverse(ptr.next, k)
            
            last_node = ptr.next
            last_node.next = curr
            ptr.next = prev
            
            ptr = last_node
        
        return dummy.next

        