'''Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.'''


# SOLUTION

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        a_pointer = head
        b_pointer = head

        while a_pointer and a_pointer.next:
            a_pointer = a_pointer.next.next
            b_pointer = b_pointer.next

            if a_pointer == b_pointer:
                return True
        return False