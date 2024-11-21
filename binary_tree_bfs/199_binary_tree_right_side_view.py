'''Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.'''

# Solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        output = []
        curr = deque([root])
        while curr:
            n = len(curr)
            val = 0
            for i in range(n):
                node = curr.popleft()
                val = node.val
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            output.append(val)
        return output