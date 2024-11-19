'''Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
'''

# SOLUTION

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        res.next = head
        curr  = res

        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                while curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                    curr.next = curr.next.next

                curr.next = curr.next.next

            else:
                curr =  curr.next

        return res.next