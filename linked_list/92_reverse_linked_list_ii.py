'''Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.'''


# SOLUTION

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head


        temp = ListNode(0, head)
        last = temp

        for i in range(left - 1):
            last = last.next
        
        currentNode = last.next
        for i in range(right - left):
            t = currentNode.next
            currentNode.next = t.next
            t.next = last.next
            last.next = t
        
        return temp.next