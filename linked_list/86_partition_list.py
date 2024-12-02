'''given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x. you should
preserve the original relative order of the nodes in each of the two partitions'''

# Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x:int) -> Optional[ListNode]:

        less = ListNode(0)
        more = ListNode(0)

        l_ptr = less
        r_ptr = more

        while head:
            if head.val < x:
                l_ptr.next, l_ptr = head, head
            
            else:
                r_ptr.next, r_ptr = head, head
            
            head = head.next
        
        r_ptr.next = None
        l_ptr.next = more.next

        return less.next