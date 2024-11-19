'''Given the head of a linked list, rotate the list to the right by k places.'''

# SOLUTION

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    # method to get length of list
    def listLength(self, node: Optional[ListNode]) -> int:
        n = 0
        while node:
            node = node.next
            n += 1
        return n
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # return empty list
        if not head:
            return head
        n = self.listLength(head)
        
        # return list if steps moved is same as list length
        if k % n == 0:
            return head
        # wrap around if k is larger than numbers in list
        k = k % n
        node = head
        for i in range(n - k - 1):
            node = node.next
        out = node.next
        node.next = None
        tail = out
        while tail.next:
            tail = tail.next
        tail.next = head
        return out