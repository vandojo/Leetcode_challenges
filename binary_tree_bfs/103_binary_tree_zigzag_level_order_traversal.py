'''Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).'''

# SOLUTION

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        zigzag = True
        output = []
        curr = deque([root])
        while curr:
            n = len(curr)
            vals = []
            
            for i in range(n):
                node = curr.popleft()
                vals.append(node.val)
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            if zigzag:
                output.append(vals)
            else:
                output.append(vals[::-1])                
            zigzag = not zigzag
            
        return output