'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

# SOLUTION

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        node = ListNode()
        currentNode = node

        while list1 and list2:

            if list1.val > list2.val:
                currentNode.next = list2
                list2 = list2.next
            else:
                currentNode.next = list1
                list1 = list1.next

            currentNode = currentNode.next
        
        if list1:
            currentNode.next = list1
        else:
            currentNode.next = list2
        
        return node.next