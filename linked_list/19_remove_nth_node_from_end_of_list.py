'''Given the head of a linked list, remove the nth node from the end of the list and return its head.'''

# Solution

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res

        for i in range(n):
            head = head.next
        
        while head:
            head = head.next
            dummy = dummy.next
        dummy.next = dummy.next.next

        return res.next