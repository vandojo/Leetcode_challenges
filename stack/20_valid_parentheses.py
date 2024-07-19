'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true
'''


# solution  
class Solution:

    def checkPair(self, lastElem: str, currentElem: str) -> bool:

        if lastElem == '(' and currentElem ==')' or lastElem == '[' and currentElem ==']' or   lastElem == '{' and currentElem =='}':
            return True

        return False

    def isValid(self, s: str) -> bool:


        stack = []

        for i in range(len(s)):

            if stack:

                if self.checkPair(lastElem=stack[-1], currentElem=s[i]):
                    stack.pop()
                    continue


            stack.append(s[i])
        
        return not stack

