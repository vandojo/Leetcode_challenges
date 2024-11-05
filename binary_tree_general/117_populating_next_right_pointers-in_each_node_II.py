'''description

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.


'''

# Solution


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        head = root

        while head:
            temp = Node()
            cur = temp

            while head:
                if head.left:
                    cur.next = head.left
                    cur = cur.next
                if head.right:
                    cur.next = head.right
                    cur = cur.next
                head = head.next
            head = temp.next
        
        return root
        