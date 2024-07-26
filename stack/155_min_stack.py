'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","

Output
[null,null,null,null,-3,null,0,-2]push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
'''

# Solution

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:

        value = self.getMin()
        if value == None or value > val:
            value = val
        self.stack.append([val, value])
        

    def pop(self) -> None:

        self.stack.pop()
        return
        

    def top(self) -> int:

        if self.stack:
            return self.stack[-1][0]
        else:
            return None
        

    def getMin(self) -> int:

        if self.stack:
            return self.stack[-1][1]
        else:
            return None